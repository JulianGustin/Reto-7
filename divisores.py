#Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

divisor : int = 1 

#Iniciar codigo 

if __name__ == "__main__": 
    numero = int(input("Ingrese un numero entre 2 y 50: "))
    if numero >= 2 and numero <=50: #Si el numero esta entre 2 y 50
    
        print (f"Los divisores de {numero} son: ") 

        #Evaluar los divisores de un numero de 1 a 1 con modulo
        while divisor <= numero: 
            s = numero % divisor 
            if s == 0: 
                print(divisor)
            divisor +=1

    else:
        print ("Su numero no esta entre 2 y 50")
        

        