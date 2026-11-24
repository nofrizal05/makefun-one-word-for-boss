"""One Word for the Boss — make.fun entry.

Writes exactly one word to /output/entry.txt: the word that describes
the boss. No phrase, no caption, no explanation. The word is the whole
entry.
"""

import os

WORD = "Escalator"


def validate(word):
    """The gate: exactly one word, 1-30 characters, not only white space."""
    assert isinstance(word, str), "word must be a string"
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word.strip() != "", "word must not be only white space"
    assert len(word.split()) == 1, "word must be a single word"


def main():
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
