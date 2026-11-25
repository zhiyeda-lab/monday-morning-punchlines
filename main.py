#!/usr/bin/env python3
"""Monday Morning Punchlines - entry for make.fun
u-gentle-badger-68-monday-morning-punchlines-709645dc.

Writes the entry joke to /output/entry.txt (and prints it).
No arguments, no network, no randomness: same output every run.
"""

import os

JOKE = (
    "Why am I so energetic on Monday mornings? "
    "I take the 401(k) to work \u2014 it drives me straight to retirement."
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        out = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        out = os.path.join("output", "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
