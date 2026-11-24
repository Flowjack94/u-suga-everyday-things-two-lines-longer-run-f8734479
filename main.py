#!/usr/bin/env python3
"""Write the two-line toaster entry to /output/entry.txt.

Competition: Everyday Things, Two Lines, Longer Run
(make.fun slug: u-suga-everyday-things-two-lines-longer-run-f8734479)

Line 1 explains a toaster to a 10-year-old in one vivid sentence built
on a single metaphor (a sunbed). Line 2 says in one sentence what the
analogy maps (heat + a timer do the browning) and what it leaves out
(bread cannot roll over or choose how dark it gets; the real sun never
pops you up with a ding).

Deterministic, no network, no external input. Runs on Python 3.13.
"""

import hashlib
import sys
from pathlib import Path

LINE_1 = "A toaster is a tiny sunbed where bread lies flat and tans until both sides turn golden brown, then pops up when its timer rings."
LINE_2 = "The sunbed fits because heat and a timer do the browning, but bread cannot roll over or choose how dark it gets, and the real sun never pops you up with a ding."

ENTRY = LINE_1 + "\n" + LINE_2
OUTPUT_PATH = Path("/output/entry.txt")

# Competition gate (Everyday Things, Two Lines, Longer Run):
# exactly 2 lines, 1-400 characters total, no trailing whitespace.
EXPECTED_LINES = 2
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 400


def validate(text: str) -> None:
    """Gate-check the entry before anything is written."""
    if not text or not text.strip():
        raise SystemExit("ERROR: entry is empty or only whitespace")
    lines = text.split("\n")
    if len(lines) != EXPECTED_LINES:
        raise SystemExit(
            f"ERROR: entry must have exactly {EXPECTED_LINES} lines, "
            f"got {len(lines)}"
        )
    if any(not line.strip() for line in lines):
        raise SystemExit("ERROR: each line must contain non-whitespace text")
    if any(line != line.rstrip() for line in lines):
        raise SystemExit("ERROR: no line may end with trailing whitespace")
    if not MIN_ENTRY_CHARS <= len(text) <= MAX_ENTRY_CHARS:
        raise SystemExit(
            f"ERROR: entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} "
            f"characters total, got {len(text)}"
        )


def main() -> int:
    # Self-test: exactly two lines, under 400 characters, not blank.
    assert ENTRY.count("\n") == 1, "entry must contain exactly one newline"
    assert len(ENTRY.split("\n")) == 2, "entry must be exactly 2 lines"
    assert len(ENTRY) < 400, f"entry too long: {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    validate(ENTRY)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly two lines joined by one "\n", no trailing newline.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")

    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} characters, 2 lines)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
