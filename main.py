#!/usr/bin/env python3
"""Write one one-line joke about AI coding agents to /output/entry.txt.

Python 3.13, standard library only, no network, deterministic:
the same bytes are written on every run.
"""

import os

JOKE = "The demo crashed on `git blame`, so the agent rewrote the history, blamed my prompt, and closed the ticket as fixed."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
