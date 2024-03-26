string = "+23-2-32+4-22-4"
broj_negativnih = sum(1 for x in string.split('-') if len(x) == 2)
print(broj_negativnih)