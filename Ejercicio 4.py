import random

def adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 10
    intento_actual = 0
    
    print("¡Bienvenido al juego Adivina el Número!")
    print("He generado un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")
    
    while intentos_restantes > 0:
        intento_actual += 1
        intentos_restantes -= 1
        
        try:
            guess = int(input(f"\nIntento #{intento_actual} (te quedan {intentos_restantes}): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
            
        if guess == numero_secreto:
            print(f"¡Felicidades! ¡Adivinaste el número en el intento #{intento_actual}!")
            return
        elif guess < numero_secreto:
            print(f"El número secreto es mayor que {guess}.")
        else:
            print(f"El número secreto es menor que {guess}.")
    
    print(f"\n¡Lo siento! Has agotado tus 10 intentos. El número secreto era {numero_secreto}.")

# Ejecutar el juego
adivina_numero()