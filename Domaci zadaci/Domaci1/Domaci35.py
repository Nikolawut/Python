f = False
while f != True:
    t = str(input("Unesite petocifreni broj:"))
    if len(t) == 5:
        f = True
print(f"Sprat je: {int(t[len(t)//2])+int(t[-1])}")