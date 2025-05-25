# AI-Selfhealing Pipeline

Experimental repo exploring how LLMs like ChatGPT could observe and assist with CI/CD troubleshooting in real time.

## Concept

- Watch CI/CD pipeline logs
- Summarize issues using an LLM
- Trigger suggestions or actions for resolution
- Close the loop via GitHub PR comments or alerts

## Stack

- GitLab CI/CD or Argo Workflows
- OpenAI API / GPT-4 / Claude
- GitOps feedback loop

## Status

Very early experimentation. Ideas > implementation.

## Goal

Learn how LLMs can support observability, triage, and operational clarity inside DevOps pipelines.

## Try It Out

This repo includes a working log parser to detect common failure patterns in CI/CD or Kubernetes logs.

**`log_parser.py`**

### Step 1: Create a test log file

```bash
echo -e "Starting deployment...\\nERROR: Helm chart failed\\nAll done." > test.log
```

### Step 2: Run the script

```bash
python log_parser.py
```

Then enter:
```
test.log
```

### Output:

```
⚠️  Detected issues:
 - ERROR: Helm chart failed
```

This simulates the first step of a self-healing pipeline — detecting issues for further automation or AI analysis.
