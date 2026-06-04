from pathlib import Path
from datetime import datetime


def read_file(file_path):
    """Read raw notes from a text file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def build_support_case(raw_notes, case_title):
    """Build a structured support case from raw troubleshooting notes."""

    current_date = datetime.now().strftime("%Y-%m-%d")

    support_case = f"""# {case_title}

## Date Created
{current_date}

## Purpose
This support case was generated from raw cybersecurity troubleshooting notes. The goal is to organize technical details into a clean format for analyst review, customer communication, internal documentation, and knowledge-base development.

## Raw Notes Provided

```text
{raw_notes}
