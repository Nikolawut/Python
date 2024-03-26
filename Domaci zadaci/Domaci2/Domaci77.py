lista = [1, 3, 5, 7, 9]
je_sortirana = all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
print("Lista je sortirana:", je_sortirana)