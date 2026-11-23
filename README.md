# Six Words, One Story

[![Built with make.fun](https://img.shields.io/badge/built%20with-make.fun-blue)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

Entry for the [make.fun](https://make.fun) competition
[Six Words, One Story](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410):
one complete story in exactly six words.

## The entry

> Her reflection smiled. She did not.

Six words, 35 characters. A woman faces her mirror; the reflection
smiles while she does not. The turn is the reflection acting on its
own, and the reader is left to fill in why — a doppelganger, a ghost,
a life lived on the wrong side of the glass.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes the story to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`, default `/output`). It checks the story is
exactly six words and within the 1–60 character gate before writing.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
