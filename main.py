"""The dog ate my homework: the defendant's sworn statement, given freely for treats."""

import os

LINE = "Your Honour, the homework smelled of bacon grease and poor supervision; it lay on the floor, and under dog law the floor is a buffet with no cover charge. I plead adorable."

# The court only accepts short statements: one line, at most 200 characters.
assert len(LINE) <= 200, "statement too long for the record"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
