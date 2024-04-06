import pandas as pd

dataset = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\GitHub\Python\Test\dataset.csv")

kolona = dataset['artists']

najveca_vrijednost = kolona.max()
najmanja_vrijednost = kolona.min()

prosjek = kolona.mean()

razlika = ((najveca_vrijednost - prosjek) / prosjek) * 100

normalized_kolona = (kolona - kolona.min()) / (kolona.max() - kolona.min())

dataset['popularity'] = normalized_kolona
korrelacija = dataset.corr()
najveca_pozitivna_korelacija = korrelacija[korrelacija != 1.0].max().idxmax()
najveca_negativna_korelacija = korrelacija[korrelacija != 1.0].min().idxmin()

print("Najveća vrijednost:", najveca_vrijednost)
print("Najmanja vrijednost:", najmanja_vrijednost)
print("Prosjek:", prosjek)
print("Procentualna razlika:", razlika)
print("Najveća pozitivna korelacija:", najveca_pozitivna_korelacija)
print("Najveća negativna korelacija:", najveca_negativna_korelacija)