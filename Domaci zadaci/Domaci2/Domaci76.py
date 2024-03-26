lista = [1, 2, 3, 2, 4, 2]
stari_element = 2
novi_element = -2
nova_lista = [novi_element if x == stari_element else x for x in lista]
print("Nova lista:", nova_lista)