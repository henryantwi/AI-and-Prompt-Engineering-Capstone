# Capstone Project: Smart Log Analyzer
## Multi-Stage AI Workflow

**Submitted by:** Henry Nana Antwi
**Date:** 2026-02-10
**Course:** Applied AI & Prompt Engineering
**AI Chat Session:** [View Full Conversation](https://gemini.google.com/share/a296ab0fb023)

---

## 1. Problem Statement

### The Challenge
Server logs are one of the most critical data sources for diagnosing system health, yet they are notoriously difficult to read manually. A typical production server generates thousands of log entries per hour across multiple severity levels (INFO, WARNING, ERROR, CRITICAL). Engineers often waste valuable time scrolling through raw text files trying to find patterns, identify recurring errors, or detect anomalous spikes.

### The Solution
A **Smart Log Analyzer** — a Python-based tool that automatically:
- Parses structured log entries using regex pattern matching
- Counts occurrences of each log level
- Identifies the **top 5 most frequent error messages**
- Categorizes entries into **severity buckets** (Low / Medium / High) with percentage breakdowns
- Detects **anomalous time periods** with unusually high error rates using statistical analysis (mean + 2σ threshold)
- Outputs a clean **JSON report** for downstream consumption
- Logs its own activity to `logs/analyzer.log` for audit trails

---

## 2. Workflow Design

### Tools Used
| Step | AI Tool | UX Type | Purpose |
|------|---------|---------|---------|
| 1 | **ChatGPT** (OpenAI) | **Chat** | Generate the base `log_analyzer.py` script and sample data |
| 2 | **VS Code Copilot** | **IDE** | Refine code: add severity summary, file-based logging, and improved structure |

### Process Flow
```
[Raw Server Logs] 
    → Step 1: ChatGPT generates log_analyzer.py (Chat UX)
        → Step 2: VS Code Copilot refines with severity + logging (IDE UX)
            → [JSON Report + Console Summary + Analyzer Logs]
```

### Data Handoff
The output of **Step 1** (a working but basic Python script) became the direct input for **Step 2** (pasted into VS Code, where the IDE AI added new features). This is the core "chaining" requirement.

---

## 3. Implementation Steps

### Step 1: Generate Base Code (Chat AI — ChatGPT)

**Goal:** Create a production-ready log analyzer from a natural language description.

**Prompt Used:**
```
I am a Data Engineer. I need a Python script called log_analyzer.py that:
1. Reads a server log file (.log format).
2. Parses each line to extract: timestamp, log level (INFO, WARNING, ERROR, CRITICAL), and message.
3. Counts how many of each log level occurred.
4. Identifies the top 5 most frequent error messages.
5. Detects time periods with unusually high error rates (anomaly detection).
6. Outputs a summary report as a JSON file (analysis_report.json).
7. Prints a clean console summary.

Use Python's re, collections, and json modules. Include logging. Make the script production-ready 
with proper error handling and docstrings. Also generate a sample server log file 
(sample_server.log) with at least 100 lines containing a mix of INFO, WARNING, ERROR, 
and CRITICAL entries.
```

**Output Summary:**
ChatGPT generated:
- `log_analyzer.py` (~200 lines) with `parse_log_line()`, `analyze_log_file()`, `detect_anomalies()`, `write_json_report()`, and `print_console_summary()` functions.
- `sample_server.log` with 26 structured log entries across all 4 severity levels.
- Statistical anomaly detection using mean + 2σ threshold.

---

### Step 2: Refine with IDE AI (VS Code Copilot)

**Goal:** Enhance the script with severity categorization and file-based logging.

**Prompt Used (in VS Code Copilot Chat):**
```
Add a new feature to this script: generate a severity summary that categorizes log entries into 
'Low' (INFO), 'Medium' (WARNING), and 'High' (ERROR + CRITICAL) with percentage breakdowns. 
Also add file-based logging so the analyzer logs its own activity to logs/analyzer.log.
```

**Output Summary:**
The IDE AI added:
- **`build_severity_summary()` function** — Categorizes all entries into Low/Medium/High buckets with precise percentage calculations.
- **File-based logging** — Created a dual-handler logging system (console + `logs/analyzer.log`) with DEBUG-level file output for audit trails.
- **Updated console summary** — Added a new "Severity Summary" section to the printed output.

**Key Changes Made by IDE AI:**

| Feature | Before (ChatGPT) | After (Copilot) |
|---------|-------------------|-----------------|
| Logging | Console only (`basicConfig`) | Console + File (`StreamHandler` + `FileHandler`) |
| Severity | Raw level counts only | Low/Medium/High with % breakdowns |
| Audit trail | None | `logs/analyzer.log` with timestamps |
| Code size | ~200 lines | ~290 lines |

---

## 4. Proof of Execution

### Test Results
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

### Generated Artifacts
- `analysis_report.json` — Machine-readable JSON report
- `logs/analyzer.log` — Analyzer's own activity log

---

## 5. Reflection

### What were the main challenges?
The biggest challenge was ensuring the **handoff** between tools was seamless. ChatGPT generated a complete, working script, but it used `logging.basicConfig()` which is a global configuration. When the IDE AI added file-based logging, it correctly replaced this with explicit `StreamHandler` and `FileHandler` instances to avoid conflicts. Understanding *why* the IDE made this architectural choice (not just *what* it changed) was a valuable learning moment.

### What did you learn about chaining AI tools?
Different AI UX types excel at different tasks:
- **Chat AI (ChatGPT)** is best for *greenfield generation* — creating something from nothing based on a high-level description. It produced a complete, functional script in one shot.
- **IDE AI (VS Code Copilot)** is best for *surgical enhancements* — it understands the existing code context (imports, class structure, function signatures) and can add features that integrate cleanly with what already exists.

Chaining them (Chat → IDE) gave me the best of both worlds: rapid prototyping + precise refinement.

### Efficiency Analysis
- **Time saved:** ~45 minutes
- **Without AI:** Writing a regex-based log parser, implementing statistical anomaly detection, building a severity classifier, and setting up dual-handler logging would take approximately 1 hour.
- **With AI workflow:** The entire process took ~15 minutes (including prompt iteration and testing).
- **Quality improvement:** The AI-generated code included features I might have skipped (e.g., `docstrings`, `type hints`, `try/except` blocks), resulting in more production-ready code.
