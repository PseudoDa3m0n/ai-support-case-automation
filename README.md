# AI Support Case Automation

## Project Overview

This project demonstrates an AI-assisted technical support workflow designed to convert raw cybersecurity troubleshooting notes into structured support documentation.

The workflow was tested using two lab scenarios from a home cybersecurity environment:

1. Nessus SSH connectivity troubleshooting
2. Nessus credentialed scan review and vulnerability triage

The goal of this project is to show how AI can help technical support and cybersecurity teams create cleaner documentation, summarize issues, draft customer-facing responses, prepare internal notes, and build reusable knowledge-base articles.

## Tools Used

* ChatGPT
* Python
* Windows PC
* VMware Workstation Pro
* Ubuntu VM
* Tenable Nessus Essentials
* Markdown documentation
* GitHub

## Project Files

| File                           | Purpose                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `support_case_builder.py`      | Python script that creates a structured support case template from raw notes |
| `prompt_template.txt`          | Reusable AI prompt for support documentation                                 |
| `sample_raw_notes_case_01.txt` | Raw notes for the Nessus SSH troubleshooting case                            |
| `sample_raw_notes_case_02.txt` | Raw notes for the Nessus credentialed scan review case                       |
| `sample_output_case_01.md`     | AI-generated output for the SSH troubleshooting case                         |
| `sample_output_case_02.md`     | AI-generated output for the scan review and triage case                      |

## Use Case

Technical support notes are often messy, incomplete, or written during live troubleshooting. This project shows how raw notes can be transformed into a consistent support case format.

The workflow generates:

* Case title
* Issue summary
* Environment details
* Symptoms
* Troubleshooting performed
* Root-cause analysis
* Resolution
* Validation steps
* Customer-facing response
* Internal support notes
* Knowledge-base article draft
* Missing information checklist

## Lab Scenario 1: Nessus SSH Connectivity Troubleshooting

In the first test case, a Nessus credentialed scan setup required SSH access to an Ubuntu VM. The Ubuntu host was reachable by ping, and SSH was running on port 22, but Windows could not connect to port 22.

After troubleshooting, the issue was traced to conflicting UFW firewall rules. The firewall had both deny and allow rules for SSH. Removing the deny rules allowed SSH connectivity, and the Nessus credentialed scan later completed successfully with authentication passing.

## Lab Scenario 2: Nessus Credentialed Scan Review

In the second test case, a completed Nessus credentialed scan was reviewed and summarized. The scan authenticated successfully against the Ubuntu VM and returned informational findings. The AI workflow helped organize the scan result into a triage summary, analyst notes, hardening guidance, and a knowledge-base draft.

## Human Review

This project uses AI to speed up documentation, but it does not replace analyst judgment.

All AI-generated output should be reviewed for:

* Accuracy
* Missing information
* Overstated risk
* Unsupported assumptions
* Correct remediation guidance
* Clear separation between confirmed facts and assumptions

## Skills Demonstrated

* AI-assisted technical support documentation
* Cybersecurity troubleshooting documentation
* Nessus scan review and triage
* Root-cause analysis
* Knowledge-base article drafting
* Python scripting basics
* Markdown documentation
* GitHub portfolio organization
* Responsible human review of AI output

## Resume Summary
Built and tested an AI-driven technical support workflow using ChatGPT and Python to convert raw cybersecurity troubleshooting and Nessus scan notes into structured support cases,
root-cause summaries, customer-facing responses, internal support notes, and reusable knowledge-base drafts.

