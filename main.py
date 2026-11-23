#!/usr/bin/env python3
"""Six Words, One Story -- make.fun entry.

Writes one complete six-word story to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output).

The story: a woman faces her mirror and the reflection smiles
while she does not. A whole uncanny life is implied in the
gap between the two sentences, and the reader is left to fill
in why.
"""

import os
import sys

# The six words, fixed at write time: deterministic, no network,
# no randomness -- the same story on every run. The turn is the
# reflection acting on its own; the second sentence leaves the
# reader to fill in why it smiles when she does not.
STORY = "Her reflection smiled. She did not."

OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 60


def validate(text):
    """Check the story meets the competition gate before writing."""
    if not text or text.isspace():
        raise ValueError("story must not be empty or only whitespace")
    chars = len(text)
    if chars < 1 or chars > MAX_CHARS:
        raise ValueError(f"story must be 1-{MAX_CHARS} characters, got {chars}")
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    return text


def main():
    story = validate(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(story)
    print(f"wrote {len(story)} characters, {len(story.split())} words to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
