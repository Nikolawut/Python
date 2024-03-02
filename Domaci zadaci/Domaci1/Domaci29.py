import math

x1 = float(input("Unesite x1 koordinatu : "))
y1 = float(input("Unesite y1 koordinatu : "))
x2 = float(input("Unesite x2 koordinatu : "))
y2 = float(input("Unesite y2 koordinatu : "))

xs = (x1 + x2) / 2
ys = (y1 + y2) / 2
r = math.sqrt((xs - x1)**2 + (ys - y1)**2)

print(f"Srednja tacka je: ({xs}, {ys})")
print(f"{x1:.2f}")
print(f"Rastojanje od pocetne tacke do sustretne je: {r:.2f}")