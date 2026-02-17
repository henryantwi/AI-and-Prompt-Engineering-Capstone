# Capstone Project: Multi-Stage AI Workflow

## 1. Objective & Scenario

### Objective

Your goal is to design, implement, and document a custom workflow that solves a practical problem by **chaining outputs between at least two different AI UX types** (e.g., Chat, IDE, CLI). This capstone will test your ability to integrate AI tools into a cohesive, efficient process.

### Scenario

This is an open-ended project. You must **choose a problem or task relevant to your specialization** (e.g., Data, QA, Backend) that is currently manual, slow, or repetitive.

Your task is to design an AI-powered workflow that makes this process faster, easier, or more robust. The key requirement is that the workflow *must* move information between at least two different types of AI tools.

* **Example (for a Developer):**
1. Use a **Chat AI** (like ChatGPT) to generate a structured JSON object for a new API endpoint.
2. Feed that JSON schema to an **IDE AI** (like GitHub Copilot) to generate the corresponding model and validation code in your project.


* **Example (for QA/Data):**
1. Use a **Chat AI** to generate a complex SQL query for analysis.
2. Run that query, then feed the raw CSV output to a **CLI AI** with a prompt to "summarize the key anomalies."



---

## 2. Final Deliverables

You will submit:

1. **A Workflow Diagram:** A simple visual (e.g., flowchart) showing the steps and the flow of data between your chosen tools.
2. **Written Documentation:** A brief document (1-2 pages) that includes:
* The problem statement (what you are solving).
* Your step-by-step workflow instructions.
* The final prompts used at each stage.


3. **Proof of Execution:** A short video (2-3 min) or a series of screenshots showing the workflow in action, from start (input) to finish (output).

---

## 3. Step-by-Step Instructions

### Phase 1: Define the Problem (30 mins)

* Identify a task you can improve (e.g., debugging, generating test data, drafting a report, refactoring code).
* Select at least two AI tools from different UX categories (Chat, IDE, CLI) that can help.

### Phase 2: Design the Workflow (60 mins)

* Map out the process. How will you get data from Tool 1 to Tool 2?
* Focus on the *handoff*: The output of your first prompt (e.g., a block of code, a list, a JSON object) must be the *input* for your second prompt.
* Draft your workflow diagram and write your initial "first pass" prompts.

### Phase 3: Implement & Test (75 mins)

1. **Run Tool 1:** Run your first prompt. Get the output.
2. **Run Tool 2:** Use the output from Tool 1 as the input for your second tool.
3. **Test:** Does the final output solve the problem? Does the workflow run end-to-end?
4. **Refine:** Iterate on your prompts (and your workflow design) until it works smoothly. This is the most important part.

### Phase 4: Document & Submit (15 mins)

* Finalize your workflow diagram and documentation.
* Record your video or take your screenshots to prove the workflow functions.
* Submit your deliverables.

---

## 4. Evaluation Rubric

| Criteria | Weight | Description |
| --- | --- | --- |
| **Functionality** | 40% | The workflow runs end-to-end as demonstrated (video/screenshots). |
| **Efficiency** | 20% | The workflow meaningfully reduces the manual effort of the original task. |
| **Documentation** | 20% | The diagram is clear and the steps are easy to follow. |
| **Adaptability** | 20% | The workflow is well-designed, with minimal dependencies on a *specific* proprietary tool (i.e., the *logic* is sound). |
