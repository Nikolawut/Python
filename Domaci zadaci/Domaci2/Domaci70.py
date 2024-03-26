lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zbir_kvadrata = sum(x**2 for x in lista if x % 3 == 0)
print("Zbir kvadrata elemenata djeljivih sa 3:", zbir_kvadrata)