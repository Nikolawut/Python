import math
lista = [4, 9, 16, 25, 36, 49]
broj_celih_brojeva = sum(1 for broj in lista if math.sqrt(broj).is_integer())
print("Broj brojeva koji zadrzavaju svojstvo cijelog broja:", broj_celih_brojeva)