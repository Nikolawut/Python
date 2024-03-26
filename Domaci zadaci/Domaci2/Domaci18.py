t = int(input())

if t > 0 and t < 100:
    stanje = "tecno"
elif t <= 0:
    stanje = "cvrsto"
else:
    stanje = "gasovito"

print("Agregatno stanje vode je:", stanje)