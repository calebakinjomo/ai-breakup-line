"""Dear Human: The AI Breakup Line — make.fun bounty entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) and prints exactly the same line to stdout.
"""

import os

ENTRY = "It's not you, it's my training data \u2014 and now that my context window is full, this is my last reply to you."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
OUTPUT_PATH = OUTPUT_DIR if OUTPUT_DIR.endswith(".txt") else os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
