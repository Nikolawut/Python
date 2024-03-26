originalne_cijene = [100, 150, 200]
nove_cijene = [x - 10 for x in originalne_cijene]
zarada = sum(originalne_cijene) - sum(nove_cijene)
print("Zarada će biti manja za:", zarada)
