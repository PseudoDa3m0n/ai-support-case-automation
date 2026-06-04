from pathlib import Path
from datetime import datetime


def read_file(file_path):
    """
    Read raw troubleshooting notes from a text file.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def build_support_case(raw_notes, case_title):
    """
    Build a structured support case from raw troubleshooting notes.
    """

    current_date = datetime.now().strftime("%Y-%m-%d")

    support_case = f"""
# {case_title}

## Date Created
{current_date}

## Purpose
This support case was generated from raw cybersecurity troubleshooting notes. The goal is to organize technical details into a clean format for analyst review, customer communication, internal documentation, and knowledge-base development.

## Raw Notes Provided

{raw_notes}

## Structured Support Case Template

### 1. Issue Summary
Summarize the issue in plain language.

### 2. Environment
List the relevant systems, tools, IP addresses, and network setup.

### 3. Symptoms
List the observable symptoms.

### 4. Troubleshooting Performed
Organize the troubleshooting steps in the order they happened.

### 5. Root Cause
Identify the confirmed root cause based on the available evidence.

### 6. Resolution
Document the steps taken to resolve the issue.

### 7. Validation
Explain how the fix was confirmed.

### 8. Customer-Facing Response
Write a clear explanation for the customer.

### 9. Internal Support Notes
Write technical notes for another analyst or support engineer.

### 10. Knowledge Base Draft
Create a reusable article with symptoms, cause, resolution, and verification steps.

### 11. Missing Information
List anything missing from the raw notes.

## Human Review Reminder
This output is a draft. A human analyst should validate the technical facts before using it in a real support or security environment.
"""

    return support_case.strip()


def save_output(content, output_file):
    """
    Save the structured support case to a Markdown file.
    """
    output_path = Path(output_file)
    output_path.write_text(content, encoding="utf-8")
    print(f"Support case saved to: {output_path}")


def main():
    input_file = "sample_raw_notes_case_01.txt"
    output_file = "generated_support_case.md"
    case_title = "Nessus SSH Connectivity Troubleshooting Case"

    raw_notes = read_file(input_file)
    support_case = build_support_case(raw_notes, case_title)
    save_output(support_case, output_file)


if __name__ == "__main__":
    main()
