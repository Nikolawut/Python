zav = [(0, 0), (10, 10)]
win = [(3, 3), (8, 8)]
if zav[0][0] <= win[0][0] <= win[1][0] <= zav[1][0] and zav[1][1] <= win[1][1] <= win[0][1] <= zav[0][1]:
    print("Zavjesa ce prekriti prozor.")
else:
    print("Zavjesa nece prekriti prozor.")