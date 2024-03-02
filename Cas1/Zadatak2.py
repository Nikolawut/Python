import math

d = 50
ar = (16, 9)

s = math.sqrt((d**2) / ((ar[1]**2) + (ar[0]**2)))
v = ar[1] * s / ar[0]
print(f"Površina ekrana monitora je: {(s * v):.2f}cm2")