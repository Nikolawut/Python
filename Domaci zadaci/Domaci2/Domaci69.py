zarade = [2000, 2500, 1800, 3000, 2200]
prosjek = sum(zarade) / len(zarade)
nova_lista = [(zarada * 1.1 if zarada < prosjek else zarada * 0.9) for zarada in zarade]
iznad_prosjeka = sum(zarada - prosjek for zarada in nova_lista if zarada > prosjek)
print("Zarada iznad prosjeka nakon promjene:", iznad_prosjeka)