niz = [-2, 7, -5, 3, 1, -4]
ab = sum(abs(x) for x in niz if x < 0 and x % 2 == 0)
print(ab)