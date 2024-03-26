m1 = int, input("Unesite poene za takmicara 1 matematika: ")
p1 = int, input("Unesite poene za takmicara 1 programiranje: ")
m2 = int, input("Unesite poene za takmicara 2 matematika: ")
p2 = int, input("Unesite poene za takmicara 2 programiranje: ")

ukupno1 = m1 + p1 

ukupno2 = m2 + p2
if ukupno1 > ukupno2 or (ukupno1 == ukupno2 and p1 > p2):
    print("Pobjednik je takmicar 1.")
else:
    print("Pobjednik je takmicar 2.")
