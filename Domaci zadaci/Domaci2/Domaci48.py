X = int(input("Unesite osnovu: "))
n = int(input("Unesite eksponent: "))
rezultat = 1
for _ in range(n):
    rezultat *= X
print("Rezultat:", rezultat)