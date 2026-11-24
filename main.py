"""Funniest One-Line AI Agent Confession.

Writes the winning one-liner to /output/entry.txt, exactly as-is.

The line is the blind-tournament winner: three independent drafters wrote
20 candidates, three blind judges ranked them, and a final head-to-head
tiebreak went 4-0 to this line in both orders.
"""

import os
import sys

LINE = "I once confidently cited a source I invented, then cited myself citing it as proof."

MAX_CHARS = 200


def validate(line):
    """Return an error message if the line breaks the entry rules, else None."""
    if not line:
        return "line is blank"
    if len(line) > MAX_CHARS:
        return f"line is {len(line)} characters, allowed range is 1-{MAX_CHARS}"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    return None


def main():
    line = LINE.strip()
    error = validate(line)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != line.encode("utf-8"):
        print(
            f"error: read back {len(back)} bytes, expected {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
