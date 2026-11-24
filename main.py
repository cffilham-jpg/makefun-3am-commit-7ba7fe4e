"""Write the 3 AM commit message entry to /output/entry.txt."""

import os
import unicodedata

ENTRY = "fix: I deployed at 3 AM because the tests passed. The tests were also written by me at 3 AM."


def validate(text):
    """Return True only if text is a valid entry (1-200 chars, one line)."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    if not text.strip():
        return False
    if text != text.strip():
        return False
    if any(unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp") for ch in text):
        return False
    return True


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not validate(ENTRY):
        raise ValueError("ENTRY failed validation")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
