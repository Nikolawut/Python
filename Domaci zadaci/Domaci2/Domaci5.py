a = float(input("Duzina prve str: "))
b = float(input("Duzina druge str: "))
c = float(input("Duzina trece str: "))

if a + b > c and a + c > b and b + c > a:
    print("Mozete napraviti bastu.")
else:
    print("Ne mozete napraviti bastu.")