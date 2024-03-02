f = False
while f != True:
    t = int(input("Unesite trocifreni broj:"))
    if len(str(t)) == 3:
        f = True
c1 = t%10
c2 = (t//10)%10
c3 = (t//100)%10
u = c1 + c2 + c3
k = c1 * c2 * c3
print(u-k)