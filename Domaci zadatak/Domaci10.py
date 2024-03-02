x1 = float(input("Unesite x koordinatu donje desne tačke: "))
y1 = float(input("Unesite y koordinatu donje desne tačke: "))

x2 = float(input("Unesite x koordinatu gornje leve tačke: "))
y2 = float(input("Unesite y koordinatu gornje leve tačke: "))

d = abs(x2 - x1)
s = abs(y2 - y1)

print(f"Obim je: {2*(d+s)}")
print(f"Povrsina je: {d*s}")