#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

A hardware wallet refuses to sign a transaction at 3 AM.
Writes the excuse to /output/entry.txt and prints it (one line).
Deterministic: same output on every run. Stdlib only.
"""

import os

ENTRY = "Nope — it's 3 AM, and I only take orders from the well-rested version of you. That version is currently unconscious."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
