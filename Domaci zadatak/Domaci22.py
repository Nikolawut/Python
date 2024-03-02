N = int(input("Ukupan broj ucenika: "))
K = int(input("Unesite broj ucenika:"))
p1 = float(input("Unesite prosjecan broj poena strane 1:"))
p2 = float(input("Unesite prosjecan broj poena strane 2:"))

pr = N / (((N - K)/p1) + (K/p2))
print(f"Prosjecan broj bodova svih ucenika: {pr:.2f}")