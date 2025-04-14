
#Creamos las tres variables de listas que vamos a usar 
lista1 = []
lista2 = []
lista3 = []

#Lista 1
print("Ingrese 5 números para la lista1:")
for i in range(5):
    numero = int(input(f"Elemento {i + 1} de lista1: "))
    lista1.append(numero)

#Lista2
print("\nIngrese 5 números para la lista2:")
for i in range(5):
    numero = int(input(f"Elemento {i + 1} de lista2: "))
    lista2.append(numero)

#Lista 3 (Suma dew la lista1 y Lista2)
for i in range(5):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)

print("\nLista1:", lista1)
print("Lista2:", lista2)
print("Lista3 (suma de lista1 y lista2):", lista3)
