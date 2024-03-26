s = str(input("Unesite string:"))
enkriptovano = ''.join('1' if c in 'aeiouAEIOU' else '0' for c in s)
print(enkriptovano)
