ocene = [7, 6, 8, 5, 9, 4]
prosjek = sum(ocena for ocena in ocene if ocena < 5) / len(ocene)
broj_ocjena_vece_od_prosjeka = sum(1 for ocena in ocene if ocena > prosjek)
print("Broj studenata sa ocjenom većom od prosjeka:", broj_ocjena_vece_od_prosjeka)