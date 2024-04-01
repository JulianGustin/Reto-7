# Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
# Definir variables
minimo : int = 1
maximo : int = 100 
respuesta : str = ""

#Iniciar codigo 

if __name__ == "__main__": 

    while respuesta != "si": # Hasta que la respuesta no sea si
        adiv = (minimo + maximo) // 2 #Punto medio entre el maximo y el minimo
        respuesta = input(f"Tu numero es {adiv}? (si, mayor, menor):")
        if respuesta == "mayor": 
            minimo = adiv + 1 #Actualizar el valor minimo
        elif respuesta == "menor": 
            maximo = adiv - 1 #Actualizar el valor maximo
        else: 
            print("Adivine tu numero, y es", str(adiv))