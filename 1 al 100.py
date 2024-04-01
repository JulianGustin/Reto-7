# imprimir un listado con los números del 1 al 100 y su respectivo cuadrado 

n : int = 0 #Inicializa a n en 0 

# Inciar el codigo 

if __name__ == "__main__": 
    while n < 100: #Mientras sea menor a 100 
        n += 1 #Suma 1 en cada iteracion 
        print(n) 
        m = n**2 # Elevar n al cuadrado
        print("Cuadrado de", str(n), ":", str(m))
