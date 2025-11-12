from pathlib import Path
from collections import Counter
import sys

data = (Path("rosalind_dna.txt").parent / "data" / "rosalind_dna.txt").read_text(encoding="utf-8")

n = len(data) # number of nucleotides


print(f"Number of elements = {n}")
print(f"{data.count("A")} {data.count("C")} {data.count("G")} {data.count("T")}")