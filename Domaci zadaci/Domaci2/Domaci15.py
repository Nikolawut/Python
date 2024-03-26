godina = int(input())  

prestupna = (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0)

if prestupna:
    print("Godina", godina, "je prestupna.")
else:
    print("Godina", godina, "nije prestupna.")