print("De nuevo suma de los elmentos de una lista")
# Wrapper
def sumaLista(arr):
    if len(arr) > 0:
        return suma(arr, len(arr) - 1)
    else:
        return 0

# Función recursiva
def suma(arr, x) -> int:
    if x == 0:
        return arr[0]
    else:
        return arr[x] + suma(arr, x - 1)

def sumaLista2(arr):
    if len(arr) > 0:
        return suma2(arr, 0, len(arr) - 1)
    else:
        return 0

def suma2(arr, x, n) -> int:
    if x == n:
        return arr[n]
    else:
        return arr[x] + suma2(arr, x + 1, n)

lista = [8, 6, 7]
z = sumaLista(lista)
print(z)  # Salida: 21

#z2 = sumaLista2(lista)
#print(z2)  # Salida: 21
