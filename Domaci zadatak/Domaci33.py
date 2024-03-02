w = float(input("Unesite sirinu poljane: "))
l = float(input("Unesite duzinu poljane: "))
s = float(input("Unesite duzinu stranice kvadrata: "))

nw = int(w // s)
nl = int(l // s)

t = nw * nl

print(f"Na poljani dimenzija {w:.2f} x {l:.2f} mozemo kreirati {t} kvadrata stranica {s:.2f}")
