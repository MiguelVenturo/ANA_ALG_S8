print("Resta y suma de lista")
def sumaresta(lista):
    if len(lista) == 0:
        return 0
    else: # si es par
        if lista[0] % 2 == 0:
            return lista[0] + sumaresta(lista[1:])
        else:
            return -lista[0] + sumaresta(lista[1:])

lista = [2, 3, 8, 1]
z = sumaresta(lista)  # 10 - 4 = 6
print(z)

 