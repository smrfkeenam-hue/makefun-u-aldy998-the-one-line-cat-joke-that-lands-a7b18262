import os

ENTRY = "My cat pushed my glass off the counter, watched it shatter, then looked at me like I should be more careful with my things."

def write_entry(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if not (1 <= len(ENTRY) < 200):
        raise ValueError("entry must be 1 to 199 characters")
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
