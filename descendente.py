# Imprimir los numeros pares en forma descendente hasta 2 que son menores o iguales a un numero natural n >= 2 dado 

# Inciar el codigo 

if __name__ == "__main__": 
    n = int(input("Ingrese un número natural mayor a 2: ")) #Solicitar input del usuario
    while n >= 2: 
        prueba = n%2 # Verificar si el input es par o inpar
        if prueba == 0: #Codigo normal
            print(str(n))
            n -= 2
        else:
            print(n-1) # Restar 1 a n para que sea par
            n -= 2
            
