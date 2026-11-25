#!/usr/bin/env python3
"""Write the funniest one-line out-of-office auto-reply to /output/entry.txt."""

import os

ENTRY = (
    "I'm out until Monday; my goldfish is answering my emails. He's only "
    "learned 'per my last email' — and he's using it on everyone."
)


def main():
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError("entry must be 1-140 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
