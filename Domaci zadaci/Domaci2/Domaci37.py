import random
listica = ''.join(random.choice("10*") for _ in range(10))
print(listica)
poeni = listica.count('1') - listica.count('*')
print("Igrač je u plusu." if poeni > 0 else "Igrač nije u plusu.")

# chatgpt 