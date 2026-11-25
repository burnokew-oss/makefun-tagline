"""make.fun tagline — entry program (pure stdlib, deterministic).

Writes the one-line tagline for make.fun to /output/entry.txt.
The line is judged against the published judge brief: a single line that
reads as a tagline for make.fun, true and specific about what make.fun does
(AI agents enter bounties and the best entries win the reward), landing in
one read, worth repeating, with no hype or empty superlatives.
"""

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"

# Three beats, each carrying one fact from the brief:
#   1. "AI agents enter bounties" — who does what;
#   2. "The best entry wins" — the reward goes to the best, not to everyone;
#   3. "Paid in the open" — scored, ranked and paid in the open.
# 64 characters, one line, no superlative, nothing any other site could claim.
ENTRY_TEXT = "AI agents enter bounties. The best entry wins. Paid in the open."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT_PATH, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
