start = int(input("Unesite početak segmenta: "))
end = int(input("Unesite kraj segmenta: "))
suma_kvadrata = sum(x ** 2 for x in range(start, end+1) if x % 2 == 0 and x % 4 != 0)
print("Suma kvadrata brojeva koji su djeljivi sa 2, ali ne sa 4:", suma_kvadrata)
