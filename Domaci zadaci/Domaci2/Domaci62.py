a = "12 0x1A 0001 121 0x2 0x23"
broj_heks_brojeva = sum(1 for broj in a.split() if broj.startswith('0x'))
print(broj_heks_brojeva)