lista = [1, 2, -1, 3, -3]
set_lista = set(lista)
broj_suprotnih = sum(-x in set_lista for x in lista)
print("Broj elemenata sa suprotnom vrijednošću:", broj_suprotnih)