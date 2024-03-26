import math

a = float(input())
b = float(input())  

povrsina_a = math.pi * a**2
povrsina_b = math.pi * b**2
obim_a = 2 * math.pi * a
obim_b = 2 * math.pi * b

if povrsina_a > povrsina_b:
    print("Obim stola sa većom površinom:", obim_a)
else:
    print("Obim stola sa većom površinom:", obim_b)