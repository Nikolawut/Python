f = False
while f != True:
    t = str(input("Unesite trocifreni broj:"))
    if len(t) == 3:
        f = True
k = int(t[0]) + int(t[1]) + int(t[2])
u = int(t[0]) * int(t[1]) * int(t[2])
print(u-k)