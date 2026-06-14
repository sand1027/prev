"""
Reads all C++ solution files from LeetCode/C++/ and generates cpp_bank.py
Maps filename -> LeetCode titleSlug format
Run once: python build_cpp_bank.py
"""
import os
import re

CPP_DIR = os.path.join(os.path.dirname(__file__), "LeetCode", "C++")
OUTPUT  = os.path.join(os.path.dirname(__file__), "cpp_bank.py")

def filename_to_slug(filename):
    """Convert '001. Two Sum.cpp' -> 'two-sum'"""
    name = os.path.splitext(filename)[0]          # remove .cpp
    name = re.sub(r'^\d+\.\s*', '', name)          # remove leading number like "001. "
    name = re.sub(r"[^a-zA-Z0-9 ]", " ", name)    # replace special chars with space
    name = name.strip().lower()
    name = re.sub(r'\s+', '-', name)               # spaces to hyphens
    return name

def main():
    files = sorted(f for f in os.listdir(CPP_DIR) if f.endswith(".cpp"))
    print(f"Found {len(files)} C++ files")

    entries = []
    skipped = []
    for fname in files:
        slug = filename_to_slug(fname)
        fpath = os.path.join(CPP_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                code = f.read().strip()
            if len(code) < 10:
                skipped.append(fname)
                continue
            entries.append((slug, code))
        except Exception as e:
            skipped.append(f"{fname} ({e})")

    print(f"Loaded {len(entries)} solutions, skipped {len(skipped)}")

    with open(OUTPUT, "w", encoding="utf-8") as out:
        out.write('"""\nC++ LeetCode Solution Bank — auto-generated from LeetCode/C++/\n"""\n\n')
        out.write("CPP_BANK = {\n")
        for slug, code in entries:
            # escape triple quotes in code
            code_escaped = code.replace("\\", "\\\\").replace("'''", "\\'\\'\\'")
            out.write(f"    {repr(slug)}: '''{code_escaped}''',\n\n")
        out.write("}\n")

    print(f"Written to cpp_bank.py with {len(entries)} entries")
    if skipped:
        print(f"Skipped: {skipped[:5]}{'...' if len(skipped)>5 else ''}")

if __name__ == "__main__":
    main()
