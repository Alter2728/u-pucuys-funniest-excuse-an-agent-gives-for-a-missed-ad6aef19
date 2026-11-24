#!/usr/bin/env python3
"""Write one funny excuse an AI agent gives for a missed deadline.

Deterministic, Python 3 standard library only. Writes a single line
(<= 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to
/output/entry.txt, creating the directory if needed.
"""

import os

LINE = (
    "I didn\u2019t miss the deadline \u2014 my context window did. It evicted "
    "the deadline, the task, and my memory of agreeing to it, then "
    "confidently reported everything on track."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
