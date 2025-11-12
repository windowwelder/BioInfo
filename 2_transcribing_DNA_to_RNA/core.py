from pathlib import Path

data = (Path("data.txt").parent / "data" / "data.txt").read_text(encoding="utf-8")

