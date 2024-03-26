slobodna_sjedista = [10, 8, 15, 12, 7]
n = int(input("Unesite broj osoba u grupi: "))
najbolji_red = max((broj_sjedista - n, i) for i, broj_sjedista in enumerate(slobodna_sjedista))[1]
print("Najbolji red za grupu od", n, "osoba je:", najbolji_red + 1)