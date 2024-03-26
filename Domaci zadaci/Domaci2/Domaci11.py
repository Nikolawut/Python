table = [(0, 0), (10, 5)]
ant = (0, 3)
if ant[0] in (table[0][0], table[1][0]) or ant[1] in (table[0][1], table[1][1]):
    print("Mrav se krece po ivici stola.")
else:
    print("Mrav ne se krece po ivici stola.")