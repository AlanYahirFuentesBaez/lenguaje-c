import math
def litros_galones(lts):
    return lts*3.78541

def galones_litros(gal):
    return gal/3.78541

print("Quiere convertir litros a galones, presione 1 o galones a litros, presione 2")
pregunta = input()
pregunta2="si"
while(pregunta2 == "si"):
    
    if(pregunta == "1"):
        litros = float(input("Ingrese los litros: "))
        print("Los galones son: ", litros_galones(litros))
        
    elif(pregunta == "2"):
        galones = float(input("Ingrese los galones: "))
        print("Los litros son: ", galones_litros(galones))

    print("Deseas volver a calcular? si/no")
    pregunta2 = input()
    
   
