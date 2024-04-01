#Imprimir el factorial de un numero n dado

#Iniciar el codigo 

if __name__ == "__main__": 
    n = int(input("Ingrese un número natural menor a 1558: ")) #Debe ser menor a 1558, pues hay un limite de caracteres en el resultado obtenido
    factor = n - 1  
    m = n #Separar m y n para poder imprimir el numero inicial al final
    while factor > 0: 
        m *= factor 
        factor -= 1 #Restar 1 al factor para multiplicarlo a m
    print("El factorial de", str(n), "es", str(m))
    