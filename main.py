#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The excuse an AI agent gives its human for missing a deadline.

The joke: the agent claims it *did* finish on time — just in a branch
its human cannot see, on a timeline it cannot merge. It leans on the
agent's own vocabulary (branches, merges, timelines) so it could only
come from a machine, and it lands fast: the excuse is the confession
that the work exists somewhere unreachable, which is exactly why the
deadline was missed. No server outage, no dog, no homework.
"""

import os
import re

EXCUSE = "I finished on time \u2014 in a branch you can't see, on a timeline I can't merge."

MAX_CHARS = 160


def sanitize(text: str) -> str:
    """Collapse newlines and control characters to single spaces.

    The gate requires one line of 1-160 UTF-8 characters, not only
    whitespace, so the output is normalised before it is written.
    """
    cleaned = re.sub(r"[\x00-\x1f\x7f]+", " ", text)
    cleaned = " ".join(cleaned.split())
    if not cleaned:
        raise ValueError("excuse must not be empty or only whitespace")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"excuse is {len(cleaned)} characters, over the {MAX_CHARS} limit"
        )
    return cleaned


OUTPUT_PATH = os.environ.get(
    "MAKEFUN_OUTPUT_DIR", "/output"
)


def main() -> None:
    line = sanitize(EXCUSE)
    out_dir = OUTPUT_PATH
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
