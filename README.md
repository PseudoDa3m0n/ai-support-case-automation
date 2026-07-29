# AI Support Case Automation

## Project Overview

This project demonstrates a beginner-friendly AI-assisted technical support documentation workflow.

The goal of this project is to take raw cybersecurity troubleshooting notes and organize them into a structured support case format that can be reviewed by an analyst.

This project is based on a real home-lab scenario involving Nessus credentialed scanning, SSH connectivity, Ubuntu firewall rules, and technical support-style documentation.

## Scenario

During a Nessus credentialed scan lab, SSH connectivity from a Windows host to an Ubuntu VM initially failed.

The Ubuntu VM was reachable by ping, and the SSH service was active and listening on port 22. However, Windows could not connect to port 22.

After troubleshooting, the issue was traced to conflicting UFW firewall rules on Ubuntu. The firewall had both deny and allow rules for SSH/port 22. Removing the deny rules allowed SSH connectivity, and the Nessus credentialed scan completed successfully with authentication passing.

## Tools Used

* ChatGPT
* Python
* Windows PC
* VMware Workstation Pro
* Ubuntu VM
* Tenable Nessus Essentials
* GitHub
* Markdown documentation

## Project Files

| File                           | Purpose                                                                   |
| ------------------------------ | ------------------------------------------------------------------------- |
| `support_case_builder.py`      | Python script that creates a structured support case draft from raw notes |
| `sample_raw_notes_case_01.txt` | Raw troubleshooting notes used as the input                               |
| `generated_support_case.md`    | Example structured support case output                                    |
| `README.md`                    | Project explanation and documentation                                     |

## Workflow

The workflow follows this structure:

1. Collect raw technical troubleshooting notes.
2. Save the notes in a text file.
3. Use a Python script to organize the notes into a structured support case template.
4. Review the generated output for accuracy.
5. Use the final documentation as a support case, internal note, or knowledge-base draft.

## Support Case Sections

The generated support case includes:

* Issue summary
* Environment details
* Symptoms
* Troubleshooting performed
* Root cause
* Resolution
* Validation
* Customer-facing response
* Internal support notes
* Knowledge-base draft
* Missing information
* Human review reminder

## Skills Demonstrated

* Basic Python scripting
* Reading and writing files with Python
* Cybersecurity troubleshooting documentation
* Nessus credentialed scan preparation
* SSH connectivity troubleshooting
* Ubuntu UFW firewall troubleshooting
* Technical support case documentation
* Markdown documentation
* GitHub portfolio organization
* Responsible human review of AI-assisted output

## Review Note

This project uses automation to help organize support documentation, but it does not replace analyst judgment.

All generated output should be reviewed for:

* Accuracy
* Missing information
* Unsupported assumptions
* Overstated risk
* Correct remediation guidance
* Clear separation between confirmed facts and assumptions

## Resume Summary

Built a beginner-friendly AI-assisted support documentation workflow using Python and ChatGPT concepts to convert raw cybersecurity troubleshooting notes into a structured support case. The project was tested using a Nessus SSH connectivity issue involving Windows, VMware Workstation Pro, Ubuntu, UFW firewall rules, and credentialed scan validation.
