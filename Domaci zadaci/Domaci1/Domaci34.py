f = False
while f != True:
    t = str(input("Unesite sestocifreni broj:"))
    if len(t) == 6:
        f = True
k = (int(t[0]) + int(t[1]) + int(t[2]) + int(t[3]) + int(t[4]) + int(t[-1]))**2
p = (int(t[2])*int(t[3]))
print(f"Indetifikacioni broj je: {k-p}")