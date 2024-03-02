f = False
while f != True:
    t = str(input("Unesite trocifreni broj:"))
    if len(t) == 3:
        f = True
print(t[::-1])