s = '01010'
pozicija = 2
if pozicija == 0:
    print(s[pozicija + 1] == '0')
elif pozicija == len(s) - 1:
    print(s[pozicija - 1] == '0')
else:
    print(s[pozicija - 1] == '0' and s[pozicija + 1] == '0')