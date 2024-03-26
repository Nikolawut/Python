n = int(input("Unesite broj n: "))
zbir_parnih = sum(i for i in range(1, n+1) if i % 2 == 0)
proizvod_neparnih = 1
for i in range(1, n+1):
    if i % 2 != 0:
        proizvod_neparnih *= i
print("Zbir parnih brojeva:", zbir_parnih)
print("Proizvod neparnih brojeva:", proizvod_neparnih)