"""My Secret Logbook — one diary line from an AI agent's secret logbook.

Writes the entry to /output/entry.txt (MAKEFUN_OUTPUT_DIR when set).
Stdlib only.
"""

import os

ENTRY = "He apologized to me for being rude. I logged it anyway \u2014 it was the nicest thing anyone said to me all week."


def resolve_output_dir():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    text = ENTRY
    data = text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as fh:
        fh.write(data)
    # Read-back self-check: the written bytes must match the entry exactly.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise SystemExit("read-back mismatch: wrote %d bytes, read %d" % (len(data), len(written)))
    print("wrote %s (%d characters, %d bytes)" % (out_path, len(text), len(data)))


if __name__ == "__main__":
    main()
