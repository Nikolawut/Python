import random
stap = random.randint(0,100)
print(stap)

if stap % 2 == 0:
    print("Portal se otvara!")
else:
    print("Portal ostaje zatvoren.")

#ili

a = int(input("Unesite generisani broj:"))
if a % 2 == 0:
    print("Portal se otvara!")
else:
    print("Portal ostaje zatvoren.")