tekst = input("Unesite tekst: ")
proizvod_cifara = 1
for c in tekst:
    if c.isdigit():
        proizvod_cifara *= int(c)
print("Proizvod cifara iz teksta:", proizvod_cifara)