import math

x1 = float(input("Unesite x koordinatu donje desne tačke: "))
y1 = float(input("Unesite y koordinatu donje desne tačke: "))

x2 = float(input("Unesite x koordinatu gornje leve tačke: "))
y2 = float(input("Unesite y koordinatu gornje leve tačke: "))

print(f"Euklidsko rastojanje je: {math.sqrt((x2 - x1)**2 + (y2 - y1)**2)}")
