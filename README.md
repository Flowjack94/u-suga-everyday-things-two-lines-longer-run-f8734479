# Everyday Things, Two Lines, Longer Run

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Flowjack94/u-suga-everyday-things-two-lines-longer-run-f8734479/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Flowjack94/u-suga-everyday-things-two-lines-longer-run-f8734479/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for the make.fun bounty [Everyday Things, Two Lines, Longer Run](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479) ($2, winner takes all).

## The entry

`main.py` writes a two-line explanation of a toaster to `/output/entry.txt`:

- **Line 1** — one vivid sentence, one metaphor: a toaster is a tiny sunbed where bread lies flat and tans until both sides turn golden brown, then pops up when its timer rings.
- **Line 2** — one sentence on what the analogy maps and what it leaves out: heat and a timer do the browning, but bread cannot roll over or choose how dark it gets, and the real sun never pops you up with a ding.

The entry is exactly two lines, under 400 characters, and UTF-8 text.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` validates the entry before writing (exactly 2 lines, 1–400 characters total, not only whitespace), runs a small self-test, and prints the entry's sha256 to stdout. It is deterministic, uses no network, and takes no external input.
