from pathlib import Path

data = (Path("data.txt").parent / "data" / "data.txt").read_text(encoding="utf-8")

print({data.translate(str.maketrans({"A":"T", "T": "A", "G": "C", "C": "G"}))[::-1]})