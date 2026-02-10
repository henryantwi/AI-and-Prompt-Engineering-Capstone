# 📊 Smart Log Analyzer

A production-ready Python tool that automatically parses server logs, detects anomalies, and generates actionable reports.

> **Built as a Capstone Project** for the Applied AI & Prompt Engineering course — demonstrating a multi-stage AI workflow (Chat AI → IDE AI).

---

## ✨ Features

- **Log Parsing** — Extracts timestamp, level, and message from structured log files using regex
- **Level Counting** — Tallies INFO, WARNING, ERROR, and CRITICAL entries
- **Severity Summary** — Categorizes entries into Low / Medium / High with percentage breakdowns
- **Top Errors** — Identifies the 5 most frequent error messages
- **Anomaly Detection** — Flags time periods with unusually high error rates (mean + 2σ)
- **JSON Reports** — Exports machine-readable analysis to `analysis_report.json`
- **Audit Logging** — Logs its own activity to `logs/analyzer.log`

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+

### Installation
```bash
# Clone the repo
git clone <repo-url>
cd capstone

# (Optional) Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### Usage
```bash
python log_analyzer.py
```

By default, the script reads `sample_server.log` and outputs to `analysis_report.json`.

### Example Output
```
====== LOG ANALYSIS SUMMARY ======
File analyzed: sample_server.log
Total lines: 26
Parsed lines: 26

Log Level Counts:
  INFO: 8
  WARNING: 3
  ERROR: 13
  CRITICAL: 2

Severity Summary:
  Low: 8 (30.77%)
  Medium: 3 (11.54%)
  High: 15 (57.69%)

Top 5 Error Messages:
  (5) Timeout while calling payment service
  (5) Failed to write audit log
  (3) Database connection failed
  (1) Disk write failure
  (1) Out of memory error

Anomalous Error Periods:
  None detected
=================================
```

---

## 📁 Project Structure

```
capstone/
├── log_analyzer.py          # Main script (~290 lines)
├── sample_server.log        # Sample input data
├── analysis_report.json     # Generated JSON report
├── logs/
│   └── analyzer.log         # Analyzer's own activity log
├── screenshots/             # Proof of execution
│   ├── image-1.png
│   ├── image-2.png
│   └── summary-output.png
├── pyproject.toml
└── README.md
```

---

## 🔧 Configuration

To analyze a different log file, update the `main()` function in `log_analyzer.py`:

```python
def main() -> None:
    input_log = "your_custom_file.log"      # ← Change this
    output_report = "your_report.json"       # ← Change this
```

### Expected Log Format
```
YYYY-MM-DD HH:MM:SS,mmm LEVEL Message text here
```

Example:
```
2026-02-10 14:00:12,553 ERROR Database connection failed
```

---

## 🧠 AI Workflow

This project was built using a **multi-stage AI workflow**:

| Step | Tool | UX Type | Task |
|------|------|---------|------|
| 1 | ChatGPT | Chat | Generated the base script + sample data |
| 2 | VS Code Copilot | IDE | Added severity summary + file-based logging |

---

## 👤 Author

**Henry Nana Antwi**
Applied AI & Prompt Engineering — 2026
