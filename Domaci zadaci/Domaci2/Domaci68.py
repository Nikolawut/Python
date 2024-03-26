zarade = [2000, 2500, 1800, 3000, 2200]
prosjek = sum(zarade) / len(zarade)
X = 100
nova_lista = [zarada + X if zarada > prosjek else zarada for zarada in zarade]
print("Nove zarade:", nova_lista)