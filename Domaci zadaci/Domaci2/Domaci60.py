start = 3
end = 9
suma_kvadrata = sum(x**2 for x in range(start, end+1) if x % 3 == 0 and x % 6 != 0)
print(suma_kvadrata)