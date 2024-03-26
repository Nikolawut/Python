plate = [500, 600, 700]
prosjek = sum(plate) / len(plate)
broj_zaposlenih_sa_vecom_platom = sum(1 for plata in plate if plata > prosjek)
print("Broj zaposlenih sa većom platom od prosjeka:", broj_zaposlenih_sa_vecom_platom)
