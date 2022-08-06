#El import es la 
import math
from  import 
def raiz_cuadrada: 
    return raiz (sqrt math(num))


def potencia_cuadrada:
    return potencia (math.pow(num,2))

print("Quiere convertir a raiz cuadrada , presione 1 o a potencia cuadrada, presione 2")
pregunta = input()

#Es una variable que va a permitir ingresar al ciclo while
pregunta2="si"

#Empieza el ciclo while
while(pregunta2 == "si"):
        
    if(pregunta == "1"):
        Raiz = float(input("Ingrese el numero: "))
        print("La raiz cuadrada: ", raiz_cuadrada(raiz))
        
    elif(pregunta == "2"):
        Potencia = float(input("Ingrese el numero: "))
        print("La potencia cuadrada: ", potencia_cuadrada(potencia))

    print("Deseas volver a calcular? si/no")
    pregunta2 = input()
    if(pregunta2=="no"):
        break
    print("Quiere convertir a raiz cuadrada, presione 1 o a potencia cuadrada, presione 2")
    pregunta = input()
    
   
