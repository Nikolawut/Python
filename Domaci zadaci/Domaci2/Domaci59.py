s = '15023'
enkriptovan_string = ''
for cifra in s:
    if int(cifra) % 2 == 0:
        enkriptovan_string += '0'
    else:
        enkriptovan_string += '1'
print(enkriptovan_string)