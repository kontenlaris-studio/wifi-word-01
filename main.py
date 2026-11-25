#!/usr/bin/env python3
"""One Word for Your Wi-Fi — writes exactly one word to /output/entry.txt.

The word: the spinner's own caption. Every freeze, every meeting,
every movie night ends on this word, trailing off mid-promise.
"""
import os

WORD = "Buffering…"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
