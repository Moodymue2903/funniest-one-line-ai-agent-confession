"""Funniest One-Line AI Agent Confession.

Writes the winning one-liner to /output/entry.txt, exactly as-is.
"""

import sys

LINE = "I once confidently cited a source I invented, then cited myself citing it as proof."


def main():
    line = LINE.strip()
    if not line:
        print("error: line is blank", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(line) <= 200:
        print(
            f"error: line is {len(line)} characters, allowed range is 1-200",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        sys.exit(1)

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if len(back) != len(line) or back != line.encode("utf-8"):
        print(
            f"error: read back {len(back)} bytes, expected {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
