# En 2022 el país A tendrá una población de 25 millones de habitantes 
# y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. 
# Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

year : int = 2022 
A : int = 25000000
B : int = 18900000

# Iniciar programa 

if __name__ == "__main__": 
    while A > B: 
        # Sumar a A y a B su porcentaje de crecimiento 
        A += A*0.02 
        B += B*0.03
        year += 1 #Sumar 1 al año 
    print ("El pais B superara en poblacion al pais A en el año", str(year), "Con poblaciones de", int(B), "y", int(A), "respectivamente" )