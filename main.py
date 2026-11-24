"""Funniest Autocorrect Fail — make.fun entry.

Writes a single line (an autocorrect fail: "broom" for "groom") to
/output/entry.txt, honouring MAKEFUN_OUTPUT_DIR.
Python 3.13 stdlib only, deterministic, no network, no file reads.
"""

import os
from pathlib import Path

ENTRY = "Please keep the broom sober until we've finished the wedding photos."

# Judging trade-off (T4 revise): kept "broom" for "groom" over the
# alternatives "magician's rabbi escaped" (rabbit -> rabbi; two sentences,
# slower to resolve) and "casserole was a real threat" (treat -> threat;
# weaker image, generic second sentence). Broom/groom wins because the
# wrong word is one letter off, instantly supplied by "wedding photos",
# and "keep the broom sober" makes the absurdity land in a single phrase.

assert (
    1 <= len(ENTRY) <= 199
    and ENTRY.strip() == ENTRY
    and "\n" not in ENTRY
    and "\r" not in ENTRY
    and ENTRY.isascii()
), "entry must be a single plain-ASCII line of 1-199 chars"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
