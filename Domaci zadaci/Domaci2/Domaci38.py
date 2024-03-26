s = "15223"
enkriptovano = ''.join('0' if int(c) % 2 == 0 else '1' for c in s)
print(enkriptovano)