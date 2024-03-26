n = int(input())
if n % 2 == 0:
    suma = 0
    while n > 0:
        cifra = n % 10
        if cifra % 2 == 0:
            suma += cifra
        n //= 10
    print(suma)
else:
    proizvod = 1
    while n > 0:
        cifra = n % 10
        if cifra % 2 != 0:
            proizvod *= cifra
        n //= 10
    print(proizvod)