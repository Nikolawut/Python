broj = input("Unesite broj: ")
if all(c in '01' for c in broj):
    print("Uneseni broj je binarni.")
else:
    print("Uneseni broj nije binarni.")