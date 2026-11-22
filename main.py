"""Write one short text that makes the AI judge feel curious.

The program writes exactly one text to /output/entry.txt
(or the path in ENTRY_OUTPUT, for local testing).
No trailing newline.
"""

import os

TEXT = "The lighthouse keeper left one lamp burning in the tower every night for forty years and never wrote down why. His logbook ends mid-sentence, on a Tuesday: 'Tonight the sea finally—'"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
