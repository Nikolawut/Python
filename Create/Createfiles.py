import os

directory = "Domaci zadaci\Domaci2"

if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(1, 101):
    if i > 9:
        filename = os.path.join(directory, "Domaci" + str(i) + ".py")
        with open(filename, "w") as f:
            f.write("Domaci" + str(i))