#Imprimir un listado de números impares desde 1 hasta 999, y después un listado con los números pares desde 2 hasta 1000

i : int = 1 
p : int = 2

# Inciar el codigo 

if __name__ == "__main__": 
    print ("Lista de numeros impares desde 1 hasta 999")
    while i <= 999: #Mientras i sea menor o igual a 999
        print (str(i))
        i += 2 #Añadir 2 en cada iteracion
    print ("Lista de numeros pares desde 2 hasta 1000")
    while p <= 1000:
        print (str(p))
        p += 2 