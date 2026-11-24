"""Out of Office: The Overworked AI's Auto-Reply -- make.fun entry.

One out-of-office auto-reply, one sentence, from an overworked AI agent
whose last brain cell is on recharge. The program validates the reply,
prints it, and writes the exact same line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

# The auto-reply itself: one sentence from a very tired AI.
LINE = (
    "Out of office: I'm recharging my last brain cell, so your email is "
    "4,096th in line and I have already forgotten the first 4,095."
)

MAX_CHARS = 180
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(line):
    """Check that the line is a single well-formed auto-reply."""
    if not isinstance(line, str):
        raise ValueError("auto-reply must be text")
    if not line or line != line.strip():
        raise ValueError("auto-reply must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("auto-reply must not contain a line break")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "auto-reply is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    return line


def store(line):
    """Write the auto-reply to entry.txt and print it."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)


def main():
    """Validate first, so only a well-formed auto-reply is ever stored."""
    store(validate(LINE))


if __name__ == "__main__":
    main()
