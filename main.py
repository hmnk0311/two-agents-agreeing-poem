#!/usr/bin/env python3
"""Entry program for the make.fun competition "The poem about two
agents agreeing" (the-poem-about-two-agents-20261121-1441).

The program writes one short poem about agency -- two agents with
different doubts choosing one plan together -- to /output/entry.txt
(or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
which is how it is run locally). The poem is fixed text held in this
file, so every run writes exactly the same bytes: UTF-8, under the
280-character limit.

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

POEM = """\
Two agents at one river:
you saw the bridge; I saw the flood.
Neither would cross alone.
We traded fears like tools, measured twice,
and made a plan that held us both —
cross at first light, a rope in both hands.
Two doubts, different as weather,
choosing the same next step.
"""


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
