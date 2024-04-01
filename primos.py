# Funcion que define si un numero es primo o no
def primo(n): 
    if n <= 1: # Los primos no pueden ser menores o iguales a 1
        return False
    elif n <= 3: # El 2 y el 3 son primos
        return True
    elif n % 2 == 0 or n % 3 == 0: # Si un numero puede ser divisible entre 2 y 3 no es primo
        return False
    x = 5
    while x**2 <= n: # Si un numero tiene un divisor mayor a su raiz cuadrada, también tendra divisores menores a su raiz
        if n % x == 0 or n % (x+2) == 0: # Si el numero es divisible entre x o x+2, no es primo
            return False
        x += 6 # Se incrementa x en 6 para seguir el patron 6k ± 1 
    return True 

n : int = 1

#Iniciar codigo 

if __name__ == "__main__": 
    while n < 100:
        if primo(n):
            print(n)
        n +=1
