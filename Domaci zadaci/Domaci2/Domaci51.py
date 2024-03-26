while True:
    loz = input("Unesite lozinku: ")
    if len(loz) < 100: 
        break
if len(loz) < 8:
    print("NO")
else:
    sadrzi_ms = any(c.islower() for c in loz)
    sadrzi_vs = any(c.isupper() for c in loz)
    sadrzi_cifre = any(c.isdigit() for c in loz)
    
    if sadrzi_ms and sadrzi_vs and sadrzi_cifre:
        print("YES")
    else:
        print(500/4)