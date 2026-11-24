"""Out of Office: The Overworked AI's Auto-Reply -- make.fun entry.

One out-of-office auto-reply, one sentence, from an overworked AI agent
whose last brain cell is on recharge. The program builds the reply,
validates it against the competition gate (1-159 characters, a single
line), prints it, and writes the exact same line to entry.txt inside
/output (or $MAKEFUN_OUTPUT_DIR when that variable is set).

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os
import sys

# Competition gate: the entry file must hold one line of 1-159 characters.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 159

# The auto-reply itself: one sentence from a very tired AI.
# Kept as one literal so the judged line can never drift apart.
ENTRY_LINE = (
    "Out of office: I'm recharging my last brain cell, so your email is "
    "4,096th in line and I have already forgotten the first 4,095."
)


def build_reply():
    """Return the auto-reply line exactly as it will be judged."""
    return ENTRY_LINE


def validate_reply(line):
    """Check that the line is a single well-formed auto-reply.

    Raises ValueError with a specific reason on the first failing check,
    so a bad line can never reach the output file.
    """
    if not isinstance(line, str):
        raise ValueError("auto-reply must be text")
    if not line or line != line.strip():
        raise ValueError("auto-reply must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("auto-reply must not contain a line break")
    length = len(line)
    if length < GATE_MIN_CHARS:
        raise ValueError("auto-reply is empty, below the 1-character minimum")
    if length > GATE_MAX_CHARS:
        raise ValueError(
            "auto-reply is %d characters, over the %d limit"
            % (length, GATE_MAX_CHARS)
        )
    return line


def resolve_output_path():
    """Return the entry.txt path for this run's output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def write_entry(line, path):
    """Write the auto-reply to entry.txt, creating the directory first."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    """Build, validate, then store and print -- in that order.

    Validation runs before any file is written, so only a well-formed
    auto-reply is ever stored or printed.
    """
    reply = validate_reply(build_reply())
    write_entry(reply, resolve_output_path())
    print(reply)
    return 0


if __name__ == "__main__":
    sys.exit(main())
