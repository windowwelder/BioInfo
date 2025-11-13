from pathlib import Path

data_path = (Path("data.txt").parent / "data" / "data.txt")

k, m, n = map(int, data_path.read_text("utf-8").split())
print(k, m, n)
A = k + m + n

Pr1 = (m/A)*((m-1)/(A-1))*0.25
Pr2 = (m/A)*(n/(A-1))*0.5
Pr3 = (n/A)*(m/(A-1))*0.5
Pr4 = (n/A)*((n-1)/(A-1))

Pr = 1 - (Pr1 + Pr2 + Pr3 + Pr4)

print(Pr)