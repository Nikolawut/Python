f = False
while f != True:
    t = str(input("Unesite cetvorocifreni broj:"))
    if len(t) == 4:
        f = True
k = (int(t[0]) + int(t[1]) + int(t[2]) + int(t[-1]))**2
print(f"Kvadrat od zbira ovih 4 cifre je: {k}.")