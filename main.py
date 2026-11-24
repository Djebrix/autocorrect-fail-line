"""Funniest Autocorrect Fail — one-line entry generator.

Writes a single funny autocorrect fail line to $ENTRY_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

# The entry: one concrete autocorrect disaster, told as the sent text.
# "cooking" becomes "corpse" — same sentence shape, opposite meaning,
# and the wrong word is impossible to miss on first read.
ENTRY_LINE = (
    "Texted my grandma 'I miss your cooking' — "
    "autocorrect sent 'I miss your corpse'."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")


if __name__ == "__main__":
    main()
