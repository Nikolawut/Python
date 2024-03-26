v = int(input("Unesite trenutno vrijeme u 24h format: "))

if (v < 6) or (13 <= v <= 17) or (v > 22):
    print("Mozete izvoditi bucne radove.")
else:
    print("Nije dozvoljeno izvodjenje bucnih radova.")