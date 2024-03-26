pr = float(input("Unesite postotak prisustva na predavanjima: "))
sr = int(input("Unesite 0 ako niste uradili sve sr uostalom unesite 1: "))

if pr> 75 and sr == 1:
    print("Student moze pristupiti ispitu.")
else:
    print("Student ne moze pristupiti ispitu.")
