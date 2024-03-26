x = float(input("Unesite x koordinatu: "))
y = float(input("Unesite y koordinatu: "))

if x > 0 and y > 0:
    print("Tacka se nalazi u prvom kvadrantu.")
elif x < 0 and y > 0:
    print("Tacka se nalazi u drugom kvadrantu.")
elif x < 0 and y < 0:
    print("Tacka se nalazi u trećem kvadrantu.")
elif x > 0 and y < 0:
    print("Tacka se nalazi u četvrtom kvadrantu.")
elif x == 0 and y != 0:
    print("Tacka se nalazi na y osi.")
elif x != 0 and y == 0:
    print("Tacka se nalazi na x osi.")