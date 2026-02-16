# Smart Log Analyzer

A Python script that parses server logs to find errors, count log levels, and detect simple anomalies.

> **Note:** This is my Capstone Project for the Applied AI & Prompt Engineering course.

---

## What It Does

This tool reads a standard server log file and breaks down what happened. It helps you answer questions like:
- "How many errors did we have today?"
- "What are the most common error messages?"
- "Did the error rate spike at any specific time?"

Specifically, it features:
- **Log Parsing:** Extracts the date, time, log level (INFO, ERROR, etc.), and message.
- **Severity Groups:** Groups logs into Low (INFO), Medium (WARNING), and High (ERROR/CRITICAL).
- **Anomaly Detection:** Flags minutes where the error count was unusually high (using a simple statistical threshold).
- **Reporting:** Saves all the data to a JSON file (`analysis_report.json`) and prints a summary to the console.

---

## Quick Start

### Setup

You need Python 3.7 or newer.

1. **Clone the repo:**
   ```bash
   git clone https://github.com/henryantwi/AI-and-Prompt-Engineering-Capstone.git
   cd capstone
   ```

2. **(Optional) Use a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

### how to Run

Run the script directly:
```bash
python log_analyzer.py
```

By default, it looks for `sample_server.log` in the same folder.

### Example Output

When you run it, you'll see a summary like this:

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

## Project Structure

- `log_analyzer.py`: The main Python script (approx. 290 lines).
- `sample_server.log`: A dummy log file I created to test the script.
- `analysis_report.json`: The output file with all the stats.
- `logs/`: Folder where the script saves its own internal logs.

---

## How It Was Built

I used a multi-stage AI workflow to build this:

1.  **ChatGPT:** gave me the initial script and the sample Log file.
2.  **VS Code Copilot:** helped me refine the code, specifically adding the "Severity Summary" feature and setting up the file logging.

---

## Author

**Henry Nana Antwi**
Applied AI & Prompt Engineering — 2026