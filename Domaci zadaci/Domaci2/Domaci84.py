kapacitet_stolova = [4, 6, 2, 8, 5]
broj_gostiju = int(input("Unesite broj gostiju: "))
potrebni_stolovi = (broj_gostiju - sum(kapacitet_stolova)) // 4 + 1
print("Potrebno je dodatno", potrebni_stolovi, "stolova.")