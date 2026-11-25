#!/usr/bin/env python3
"""Entry program for the One-Line Office Joke: 24-Hour Sprint bounty.

Writes one office joke (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The joke is an escalation: the meeting should have been an email,
the email a text, and the text a thought nobody had -- each step
shrinks the communication and lands the laugh on the last clause.
"""

import os

JOKE = (
    "This meeting should have been an email, the email should "
    "have been a text, and the text should have been a thought "
    "nobody had."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
