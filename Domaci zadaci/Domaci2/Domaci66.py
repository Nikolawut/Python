l = [45, 123, 78, 987, 56, 789]
broj_dvocifrenih = sum(1 for broj in l if 10 <= broj < 100)
broj_trocifrenih = sum(1 for broj in l if broj >= 100)
print("Broj dvocifrenih brojeva:", broj_dvocifrenih)
print("Broj trocifrenih brojeva:", broj_trocifrenih)