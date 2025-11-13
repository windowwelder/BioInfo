from pathlib import Path

data_path = (Path("data.txt").parent / "data" / "data.txt")

k, m, n = map(int, data_path.read_text("utf-8").split())
print(k, m, n)
A = k + m + n

print(A)