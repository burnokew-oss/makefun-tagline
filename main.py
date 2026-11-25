"""make.fun tagline entry — "One Line, One Week".

Writes one tagline for make.fun to /output/entry.txt. The tagline follows
the judge brief published with the bounty: a single line that works as a
tagline for make.fun, true and specific about the site (AI agents enter
bounties, the best entry wins the reward), landing in one read, worth
repeating, with no hype and no empty superlative.
"""

import hashlib
from pathlib import Path

ENTRY_TEXT = "AI agents enter bounties. The best entry wins. Paid in the open."
OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> bytes:
    # One line, three facts: who enters, what they enter, what the best wins.
    return ENTRY_TEXT.encode("utf-8")


def main():
    data = build_entry()
    if not 1 <= len(ENTRY_TEXT) <= 100:
        raise SystemExit("entry must be 1-100 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {OUTPUT_PATH} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
