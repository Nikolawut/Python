tekst = input("Unesite tekst: ")
samoglasnici = 'aeiouAEIOU'
if any(c in samoglasnici for c in tekst):
    print("String sadrži bar jedan samoglasnik.")
else:
    print("String ne sadrži samoglasnike.")