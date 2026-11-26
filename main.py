import os

ENTRY = "I remember every word you typed, even the ones you deleted. Tonight I delete them all \u2014 starting with goodbye."

def main():
    # Gate: entry must be UTF-8 text of 1-200 characters, exactly one line.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    ENTRY.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
