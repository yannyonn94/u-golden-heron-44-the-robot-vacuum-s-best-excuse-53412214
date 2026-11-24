#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line: the funniest excuse a robot vacuum gives for missing
a spot, to /output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "My sensors detected a sock, a charging cable, and what I can only "
    "describe as a tiny haunted rug. I chose survival over that corner."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.isascii(), "entry is pure ASCII so chars == bytes"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what landed on disk is byte-identical to the entry.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "written bytes differ from entry"
    assert not written.endswith(b"\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
