import math
def raiz_cuadrada(n):
    raiz = math.sqrt(n)    
    return raiz


def potencia_cuadrada(m):
    potencia=math.pow(m,2)
    return potencia 

print("Quiere convertir a raiz cuadrada , presione 1 o a potencia cuadrada, presione 2")
pregunta = input()

#Es una variable que va a permitir ingresar al ciclo while
pregunta2="si"

#Empieza el ciclo while
while(pregunta2 == "si"):    
        
    if(pregunta == "1"):
        Raiz = float(input("Ingrese el numero: "))
        print("La raiz cuadrada: ", raiz_cuadrada(Raiz))
        
    elif(pregunta == "2"):
        Potencia = float(input("Ingrese el numero: "))
        print("La potencia cuadrada: ", potencia_cuadrada(Potencia))

    pregunta2 = input("Deseas volver a calcular? si/no: ")
    if(pregunta2=="no"):
        break
    
    print("Quiere convertir a raiz cuadrada , presione 1 o a potencia cuadrada, presione 2")
    pregunta = input()
    
   
