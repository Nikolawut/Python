stranica_a = float(input())
stranica_b = float(input())

if stranica_a == stranica_b:
    print("Ne mogu se napraviti bar dva kvadrata.")
elif stranica_a > stranica_b:
    kvadrat1 = stranica_b ** 2
    kvadrat2 = (stranica_a - stranica_b) ** 2
    print("Mogu se napraviti dva kvadrata površina:", kvadrat1, "i", kvadrat2)
else:
    kvadrat1 = stranica_a ** 2
    kvadrat2 = (stranica_b - stranica_a) ** 2
    print("Mogu se napraviti dva kvadrata površina:", kvadrat1, "i", kvadrat2)
