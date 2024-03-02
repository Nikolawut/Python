import math 

x1 = int(input("Unesite x1 koordinatu:"))
y1 = int(input("Unesite y1 koordinatu:"))

x2 = int(input("Unesite x2 koordinatu:"))
y2 = int(input("Unesite y2 koordinatu:"))

xb = x2 + 2
yb = y2 - 3
dk = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"kordinate blaga su: T({xb},{yb})")
print(f"Vazdusno rastojanje od blaga do hrasata je:{round(math.sqrt((xb - x1)**2 + (yb - y1)**2))}")
print(f"Rastojanje od blaga do hrasta sa obilazenjem kuce:{dk + 2 + 3}") 


