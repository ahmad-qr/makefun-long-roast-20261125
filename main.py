"""One satirical sentence about lawmakers and the file they cannot convert.

Writes the sentence to /output/entry.txt for make.fun's
"The Long Roast: Lawmakers and the File They Cannot Convert" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "The committee that wants to regulate artificial intelligence spent "
    "three hours trying to convert a PDF to a Word document, then passed "
    "a law requiring the internet to print everything in triplicate."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 320 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 320, "line must be 1-320 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
