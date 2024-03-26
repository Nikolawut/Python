broj = int(input("Unesite broj: "))
suma_cifara = sum(int(c) for c in str(abs(broj)))
print("Suma cifara broja:", suma_cifara)