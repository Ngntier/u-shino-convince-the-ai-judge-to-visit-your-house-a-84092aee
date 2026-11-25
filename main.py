#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House: A Letter in One Image.

Writes the finished invitation letter image (letter.png, shipped in this
repository) to <MAKEFUN_OUTPUT_DIR>/entry.png. The copy is byte-identical
on every run: the output is a verbatim copy of the shipped file.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "letter.png")
    # Guard against a corrupted/truncated source: a PNG must start with
    # its 8-byte signature; refuse to emit an invalid entry image.
    with open(src, "rb") as f:
        signature = f.read(8)
    if signature != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{src} is not a valid PNG file")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"Wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
