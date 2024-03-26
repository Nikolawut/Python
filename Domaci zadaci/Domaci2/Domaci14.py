cijena_a = float(input())
cijena_b = float(input()) 
cijena_c = float(input())  

parovi = [(cijena_a, cijena_b), (cijena_a, cijena_c), (cijena_b, cijena_c)]
par = min(parovi, key=sum)

print("Par proizvoda sa najmanjom zbirom cijena:", par)