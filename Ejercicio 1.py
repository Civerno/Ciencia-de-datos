lista = []  #Creamnos la variable donde guardaremos la lista

while True:
    numero = int(input("Ingrese un número (negativo para terminar): "))  #Mostramos un Input para poder ingresar los numeros
    
    if numero < 0:
        break  # #Para que finalice con un numero negativo, ponemos que si se mete un numero menor que 0 se termina el While y de una muestra el print
    
    lista.append(numero)  # Agregamos el número a la lista

# Mostramos todos los números introducidos
print("Los números que introdujo fueron:", lista)

