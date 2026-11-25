#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the one line a gamer texts the boss to skip work on GTA 6 launch
week: a gas safety check in a 9-11 morning window, and someone has to be
home or it costs a 60-pound callout fee. Boring, specific, and almost
believable - which is exactly the point.
"""

import os

ENTRY = "can't come in tomorrow, gas safety check 9-11, someone has to be home or it's a £60 callout"


def main() -> None:
    # Guard the judged text: one line, at most 20 words, 1-140 chars.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    words = ENTRY.split()
    if not words or len(words) > 20:
        raise ValueError("entry must be 1-20 words")
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be 1-140 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
