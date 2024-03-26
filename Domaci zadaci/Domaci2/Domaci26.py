broj = input("Unesite broj: ")
if broj.startswith("0b"):
    print("Uneseni broj je binarni.")
elif broj.startswith("0o"):
    print("Uneseni broj je oktalni.")
elif broj.startswith("0x"):
    print("Uneseni broj je heksadecimalni.")
else:
    print("Uneseni broj je dekadni.")