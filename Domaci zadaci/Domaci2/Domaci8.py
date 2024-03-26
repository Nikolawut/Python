
p = float(input("Unesite prosjek ucenika: "))
uspjeh = ""

if p > 5:
    uspjeh = "Uspjeh nije validan."
elif p >= 4.5:
    uspjeh = "Odlican"
elif 3.5 <= p < 4.5:
    uspjeh = "Vrlo dobar"
elif 2.5 <= p < 3.5:
    uspjeh = "Dobar"
elif 2 <= p < 2.5:
    uspjeh = "Dovoljan"
else:
    uspjeh = "Nedovoljan"

print(f"Uspjeh ucenika je: {uspjeh}")