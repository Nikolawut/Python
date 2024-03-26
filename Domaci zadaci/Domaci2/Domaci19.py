a = float(input())
b = float(input())
c = int(input())

popust = 0

if b == 5.0:
    popust = a * 0.4
elif b >= 4.0:
    popust = a * 0.2
elif b >= 3.0:
    popust = a * 0.1

if c == 1:
    popust = max(popust, a * 0.3)

iznos_placanja = a - popust
print(round(iznos_placanja))