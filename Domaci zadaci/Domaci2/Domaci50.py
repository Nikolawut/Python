a = str(input("Unesite string:"))
b = ''.join(i for i in a if i in "aeiouAEIOU")
print(b)