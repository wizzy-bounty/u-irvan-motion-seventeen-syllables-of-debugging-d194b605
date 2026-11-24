#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to /output/entry.txt: three lines
in the 5-7-5 syllable shape, seventeen syllables in all. The scene is
rubber-duck debugging: you explain the code out loud, line by line,
and somewhere in your own voice the bug gives itself away.
"""

import os
import sys

LINES = [
    "Talking to the duck,",
    "I read forty lines out loud —",
    "and hear my own bug.",
]


def check_entry(written):
    if (
        len(written.splitlines()) != 3
        or not (1 <= len(written) <= 200)
        or not written.strip()
    ):
        print(
            "error: entry.txt must be 3 lines, 1-200 characters, not blank",
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = "\n".join(LINES) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    check_entry(written)


if __name__ == "__main__":
    main()
