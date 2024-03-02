import math

a = int(input("Unesite vrijednost a:"))
b = int(input("Unesite vrijednost b:"))
c = int(input("Unesite vrijednost c:"))

sq = math.sqrt(abs(b**2 - 4*a*c))
print(f"x1 je: {(-b + sq)/(a*2)}")
print(f"x2 je: {(-b - sq)/(a*2)}")