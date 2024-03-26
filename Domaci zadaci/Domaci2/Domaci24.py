tekst = input("Unesite tekst: ")
if len(tekst) > 30:
    skraceni_tekst = tekst[:27] + "..."
    print(skraceni_tekst)
else:
    print(tekst)