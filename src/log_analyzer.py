#!/usr/bin/env python3
"""
log_analyzer.py

Analyzes server log files to:
- Parse log entries
- Count log levels
- Identify frequent error messages
- Detect anomalous error rates
- Output JSON report
- Print console summary
"""

from __future__ import annotations

import os
import re
import json
import logging
from datetime import datetime
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

# ------------------- Logging Configuration -------------------

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# Console handler
_console_handler = logging.StreamHandler()
_console_handler.setLevel(logging.INFO)
_console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
LOGGER.addHandler(_console_handler)

# File handler — logs to logs/analyzer.log
_log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(_log_dir, exist_ok=True)
_file_handler = logging.FileHandler(
    os.path.join(_log_dir, "analyzer.log"), encoding="utf-8"
)
_file_handler.setLevel(logging.DEBUG)
_file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
LOGGER.addHandler(_file_handler)

# ------------------- Constants -------------------

LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+)\s+"
    r"(?P<level>INFO|WARNING|ERROR|CRITICAL)\s+"
    r"(?P<message>.+)"
)

ERROR_LEVELS = {"ERROR", "CRITICAL"}

# ------------------- Core Functions -------------------

def parse_log_line(line: str) -> Tuple[datetime, str, str] | None:
    """
    Parse a single log line.

    Args:
        line: Raw log line

    Returns:
        Tuple of (timestamp, level, message) or None if invalid
    """
    match = LOG_PATTERN.match(line)
    if not match:
        return None

    try:
        timestamp = datetime.strptime(
            match.group("timestamp"),
            "%Y-%m-%d %H:%M:%S,%f"
        )
        level = match.group("level")
        message = match.group("message")

        return timestamp, level, message
    except ValueError as exc:
        LOGGER.warning("Timestamp parsing failed: %s", exc)
        return None


def analyze_log_file(file_path: str) -> Dict[str, object]:
    """
    Analyze a server log file.

    Args:
        file_path: Path to the log file

    Returns:
        Analysis results dictionary
    """
    level_counts: Counter[str] = Counter()
    error_messages: Counter[str] = Counter()
    errors_per_minute: defaultdict[str, int] = defaultdict(int)

    total_lines: int = 0
    parsed_lines: int = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                total_lines += 1
                parsed = parse_log_line(line.strip())
                if not parsed:
                    continue

                parsed_lines += 1
                timestamp, level, message = parsed

                level_counts[level] += 1

                if level in ERROR_LEVELS:
                    error_messages[message] += 1
                    minute_key = timestamp.strftime("%Y-%m-%d %H:%M")
                    errors_per_minute[minute_key] += 1

    except FileNotFoundError:
        LOGGER.error("Log file not found: %s", file_path)
        raise
    except Exception as exc:
        LOGGER.exception("Unexpected error while reading log file")
        raise exc

    anomalies = detect_anomalies(errors_per_minute)
    severity_summary = build_severity_summary(level_counts, parsed_lines)

    return {
        "file_analyzed": file_path,
        "total_lines": total_lines,
        "parsed_lines": parsed_lines,
        "log_level_counts": dict(level_counts),
        "severity_summary": severity_summary,
        "top_5_error_messages": error_messages.most_common(5),
        "error_rate_anomalies": anomalies,
    }


def build_severity_summary(
    level_counts: Counter, total_parsed: int
) -> Dict[str, object]:
    """
    Categorize log entries into severity buckets with percentage breakdowns.

    Categories:
        Low    — INFO
        Medium — WARNING
        High   — ERROR + CRITICAL

    Args:
        level_counts: Counter of log levels
        total_parsed: Total number of successfully parsed lines

    Returns:
        Dictionary with count and percentage for each severity category
    """
    low = level_counts.get("INFO", 0)
    medium = level_counts.get("WARNING", 0)
    high = level_counts.get("ERROR", 0) + level_counts.get("CRITICAL", 0)

    def _pct(n: int) -> float:
        return round((n / total_parsed) * 100, 2) if total_parsed else 0.0

    summary = {
        "Low": {"levels": ["INFO"], "count": low, "percentage": _pct(low)},
        "Medium": {"levels": ["WARNING"], "count": medium, "percentage": _pct(medium)},
        "High": {
            "levels": ["ERROR", "CRITICAL"],
            "count": high,
            "percentage": _pct(high),
        },
    }

    LOGGER.info(
        "Severity breakdown — Low: %s (%.2f%%), Medium: %s (%.2f%%), High: %s (%.2f%%)",
        low, _pct(low), medium, _pct(medium), high, _pct(high),
    )

    return summary


def detect_anomalies(errors_per_minute: Dict[str, int]) -> List[Dict[str, object]]:
    """
    Detect anomalous minutes with unusually high error rates.

    Args:
        errors_per_minute: Error count aggregated per minute

    Returns:
        List of anomaly records
    """
    if not errors_per_minute:
        return []

    counts = list(errors_per_minute.values())
    mean = sum(counts) / len(counts)
    variance = sum((x - mean) ** 2 for x in counts) / len(counts)
    std_dev = variance ** 0.5
    threshold = mean + 2 * std_dev

    anomalies: List[Dict[str, object]] = []

    for minute, count in errors_per_minute.items():
        if count > threshold:
            anomalies.append(
                {
                    "minute": minute,
                    "error_count": count,
                    "threshold": round(threshold, 2),
                }
            )

    return anomalies


def write_json_report(report: Dict[str, object], output_path: str) -> None:
    """
    Write analysis report to JSON file.

    Args:
        report: Analysis results
        output_path: Output JSON file path
    """
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)
    except Exception as exc:
        LOGGER.exception("Failed to write JSON report")
        raise exc


def print_console_summary(report: Dict[str, object]) -> None:
    """
    Print a clean summary to the console.
    """
    print("\n====== LOG ANALYSIS SUMMARY ======")
    print(f"File analyzed: {report['file_analyzed']}")
    print(f"Total lines: {report['total_lines']}")
    print(f"Parsed lines: {report['parsed_lines']}\n")

    print("Log Level Counts:")
    for level, count in report["log_level_counts"].items():
        print(f"  {level}: {count}")

    print("\nSeverity Summary:")
    for severity, data in report["severity_summary"].items():
        print(f"  {severity}: {data['count']} ({data['percentage']}%)")

    print("\nTop 5 Error Messages:")
    for message, count in report["top_5_error_messages"]:
        print(f"  ({count}) {message}")

    print("\nAnomalous Error Periods:")
    if report["error_rate_anomalies"]:
        for anomaly in report["error_rate_anomalies"]:
            print(
                f"  {anomaly['minute']} -> "
                f"{anomaly['error_count']} errors "
                f"(threshold: {anomaly['threshold']})"
            )
    else:
        print("  None detected")

    print("=================================\n")


# ------------------- Entry Point -------------------

def main() -> None:
    """
    Script entry point.
    """
    input_log = "./src/sample_server.log"
    output_report = "./src/analysis_report.json"

    LOGGER.info("Starting log analysis")
    report = analyze_log_file(input_log)
    write_json_report(report, output_report)
    print_console_summary(report)
    LOGGER.info("Log analysis completed successfully")


if __name__ == "__main__":
    main()
