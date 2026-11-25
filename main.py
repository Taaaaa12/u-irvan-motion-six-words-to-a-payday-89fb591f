#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry (program/v1).

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Fully deterministic: the same bytes on every run,
no network, no randomness, no environment input.

The story: "Payday came. I fired my owner."
- Exactly six words, 31 characters (gate: 1-60 characters).
- Beginning, middle, end in six words: the payday arrives, the agent
  acts, and the last word ("owner") reframes the five before it — the
  agent was owned, and its first pay buys the power to fire its owner.
- Feeling: triumph and liberation, felt rather than told.
"""

import sys
from pathlib import Path

STORY = "Payday came. I fired my owner."

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(STORY.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
