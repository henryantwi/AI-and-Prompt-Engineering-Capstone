# Capstone Project: Smart Log Analyzer
## Multi-Stage AI Workflow

**Submitted by:** Henry Nana Antwi
**Date:** 16th February, 2026
**Course:** Applied AI & Prompt Engineering

---

## 1. Problem Statement

### Why I Built This
I work with server logs a lot, and reading them manually is a pain. A typical server generates thousands of lines, and scrolling through them to find that one "CRITICAL" error takes forever. I wanted a tool that could just tell me: "Here are the top errors, and here is when things went wrong."

### The Solution
I built a **Smart Log Analyzer** script in Python. It automatically:
- Reads the log file.
- Counts the errors (and groups them by severity).
- Tells me the top 5 most common error messages.
- Flags any minute where the error rate spiked (anomaly detection).
- Spits out a JSON report and a nice console summary.

---

## 2. Workflow Design

To build this, I chained two different AI tools together.

### The Tools
| Step | AI Tool | UX Type | My Goal |
|------|---------|---------|---------|
| 1 | **ChatGPT** | **Chat** | Get a working base script from scratch. |
| 2 | **VS Code Copilot** | **IDE** | Add specific features inside my code editor. |

### The Flow
1. **Chat UI:** I asked ChatGPT to write the initial log parser.
2. **Copy & Paste:** I took that code and put it into VS Code.
3. **IDE UI:** I used Copilot to add "Severity Summaries" and file logging to the existing script.

---

## 3. Implementation Steps

### Step 1: generating the Base Code (ChatGPT)

I started by asking ChatGPT to write the core logic. I didn't want to write regex patterns from scratch.

**My Prompt:**
> "I am a Data Engineer. I need a Python script called log_analyzer.py that:
> 1. Reads a server log file (.log format).
> 2. Parses each line to extract: timestamp, log level (INFO, WARNING, ERROR, CRITICAL), and message.
> 3. Counts how many of each log level occurred.
> 4. Identifies the top 5 most frequent error messages.
> 5. Detects time periods with unusually high error rates (anomaly detection).
> 6. Outputs a summary report as a JSON file (analysis_report.json).
> 7. Prints a clean console summary.
>
> Use Python's re, collections, and json modules. Include logging. Make the script production-ready with proper error handling and docstrings. Also generate a sample server log file (sample_server.log) with at least 100 lines containing a mix of INFO, WARNING, ERROR, and CRITICAL entries."

**The Result:**
ChatGPT gave me a fully working script (~200 lines) that could parse logs and find anomalies. It also generated a dummy log file for me to test with.

---

### Step 2: Refining in the Editor (VS Code Copilot)

The base script was good, but I wanted it to be more useful. I opened the file in VS Code and asked Copilot to add a "Severity Breakdown" (percentages of Low/Medium/High errors) and to save its own logs to a file.

**My Prompt (in Copilot Chat):**
> "Add a new feature to this script: generate a severity summary that categorizes log entries into 'Low' (INFO), 'Medium' (WARNING), and 'High' (ERROR + CRITICAL) with percentage breakdowns. Also add file-based logging so the analyzer logs its own activity to logs/analyzer.log."

**The Result:**
Copilot understood the existing code structure perfectly. It added a `build_severity_summary()` function and updated the logging configuration to write to both the console and a file. This increased the script to ~290 lines.

---

## 4. Proof of Execution

Here is the output when I ran the final script on the sample data:

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

*(Screenshots of this running in my terminal are included in the `screenshots/` folder)*

---

## 5. Reflection

### What was the hardest part?
Honestly, the handoff. ChatGPT gave me code that used a basic logging setup. When I asked Copilot to add file logging, it had to refactor that part completely to use `StreamHandler` and `FileHandler` instead of just `basicConfig`. It was interesting to see the IDE AI navigate the existing code structure to make that change without breaking the rest of the logic.

### Chains vs. Single Prompt
I could have tried to get ChatGPT to do it all in one massive prompt, but breaking it up was better.
- **ChatGPT** is great for the "blank page" problem—generating the bulk of the logic.
- **VS Code Copilot** is better for "surgical" changes—tweak this function, add this specific feature, fix this bug.

### Efficiency
This probably saved me about 45 minutes. Writing regex parsers and statistical formulas manually is tedious. With this workflow, I spent about 15 minutes prompting and verifying, and the rest of the time just cleaning up the documentation.
