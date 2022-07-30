#El import es la 
import math

#def nos sirve para definir funciones
def litros_galones(lts):
    return lts*3.78541

#esta funcion sirve para convertir galones a litros y se puede usar
#en cualquier parte del programa
def galones_litros(gal):
    return gal/3.78541

#La funcion print(), sirve para imprimir en pantalla
print("Quiere convertir litros a galones, presione 1 o galones a litros, presione 2")

#La funcion inut() sirve para pedirle al usuario que ingrese un valor,(Entrada de datos)
pregunta = input()

#Es una variable que va a permitir ingresar al ciclo while
pregunta2="si"

#Empieza el ciclo while
while(pregunta2 == "si"):
        
    if(pregunta == "1"):
        litros = float(input("Ingrese los litros: "))
        print("Los galones son: ", litros_galones(litros))

    elif(pregunta == "2"):
        galones = float(input("Ingrese los galones: "))
        print("Los litros son: ", galones_litros(galones))

    print("Deseas volver a calcular? si/no")
    pregunta2 = input()
    if(pregunta2=="no"):
        break#break es la sentencia que rompe el ciclo en el momento que se le indique
    print("Quiere convertir litros a galones, presione 1 o galones a litros, presione 2")
    pregunta = input()
    
   
