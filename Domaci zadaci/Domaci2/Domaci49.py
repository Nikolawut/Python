string = input("Unesite string: ")
duzina = int(input("Unesite dužinu: "))
skraceni_string = string[:duzina]
if len(string) > duzina:
    skraceni_string += "..."
print(skraceni_string)