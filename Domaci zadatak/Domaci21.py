f = 0
while f != 1:
    t = str(input("Unesite cetvorocifreni broj:"))
    if len(t) == 4:
        break
a,b = int(t[0]),int(t[-1])
a1,b1 = int(t[1]), int(t[2])
u = a**2 + 2*a*b + b**2
k = (a1+b1)*(a1-b1)
print(u-k)