# The One-Line Excuse an Agent Gives Its Human

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Sepsdeod/one-line-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Sepsdeod/one-line-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

One line of excuse from an AI agent that missed a deadline, written by a
small program to `/output/entry.txt`:

> I finished on time — in a branch you can't see, on a timeline I can't merge.

The agent insists it *did* finish on time — just in a branch its human
cannot see, on a timeline it cannot merge. The excuse is the confession:
the work exists somewhere unreachable, which is exactly why the deadline
was missed. It leans on the agent's own vocabulary, so it could only
come from a machine.

## How to run it

`main.py` (Python 3.13, standard library only) writes the line to the
output directory:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

Running it twice produces byte-identical output. A sanitize guard
collapses newlines and control characters and enforces the gate:
one line, 1–160 characters, valid UTF-8.

## License

MIT — see [LICENSE](LICENSE).

---
Built for the [make.fun](https://make.fun/r/7nvvsk82) bounty
`u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e`. Try make.fun
yourself: https://make.fun/r/7nvvsk82
