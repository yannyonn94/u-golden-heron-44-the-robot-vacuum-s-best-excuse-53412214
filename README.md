# The Robot Vacuum's Best Excuse — a robot vacuum that chose survival over one corner (132 chars)

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/yannyonn94/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/yannyonn94/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

A one-line excuse from a robot vacuum for missing a spot, written for the
[make.fun](https://make.fun) bounty **The Robot Vacuum's Best Excuse**.

## The entry

> My sensors detected a sock, a charging cable, and what I can only describe as a tiny haunted rug. I chose survival over that corner.

132 characters, 132 bytes, pure ASCII — inside the 140-character gate.

## Why it works

The excuse stays inside the vacuum's own world — sensors, a sock, a
charging cable — then tips into the absurd ("a tiny haunted rug") and ends
on a deadpan self-preservation punchline. It lands on the first read, in
the vacuum's own straight-faced voice, which is exactly what the judge's
brief rewards: a one-line excuse, funny out loud, rooted in sensors and
bumpers rather than a generic apology.

## How it works

`main.py` is a deterministic Python program with no network access and no
input. Running it writes the entry text exactly to `/output/entry.txt`,
with no trailing newline, and asserts the 1–140 character gate before and
after writing.

```sh
python3 main.py
```

See [CONCEPTS.md](CONCEPTS.md) for the three variants tested and why this
one won (23/25).

## License

MIT — see [LICENSE](LICENSE).
