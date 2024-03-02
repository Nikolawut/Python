f = False
while f != True:
    t = str(input("Unesite sestocifreni broj:"))
    if len(t) == 6:
        f = True
if int(t[0]) * int(t[2]) / 2 / int(t[-1]) == int(t[1]) / int(t[3]) * int(t[-1]):
    print ("True")
else:
    print("False")