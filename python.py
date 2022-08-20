import math

def potencia_cuadrada(m):
    potenciaCuadrada=math.pow(m,2)
    return potenciaCuadrada

def potencia_cubica(m):
    potenciaCubica=math.pow(m,3)
    return potenciaCubica

def area_circulo(radioCirculo):
    areaCirculo=((math.pi)*potencia_cuadrada(radioCirculo))
    return areaCirculo

def volumen_esfera(radioEsfera):
    volumen=((4/3)*(math.pi*potencia_cubica(radioEsfera)))
    return volumenEsfera

def raiz_cuadrada(n):
    raiz = math.sqrt(n)    
    return raiz


def area_triangulo(b,h):
    area=(b*h)/2
    return area

def area_rombo(D,d):
    area=(D*d)/2
    return area


print("Ingresa cuanto mide el radio del circulo:")
radioC=float(input())
areaCirculo=area_circulo(radioC)
print("El area del circulo es:",areaCirculo)

print("Ingresa cuanto mide el radio de la esfera:")
radioE=float(input())
volumenEsfera=volumen_esfera(radioE)
print("El volumen de la esfera es:",volumenEsfera)


#area de un cuadrado
print("Ingresa cuanto mide tu cuadrado:")
lado=float(input())
areaCuadrado=potencia_cuadrada(lado)
print("El area del cuadrado es:",areaCuadrado)

#volumen cubo
print("Ingresa cuanto mide el lado de tu cubo:")
lado=float(input())
areaCuadrado=potencia_cuadrada(lado)
volumenCubo=areaCuadrado*lado
print("El volumen del cubo es:",volumenCubo)

pi=3.1416
#area de un circulo
#volumen de la esfera



print("Ingresa cuanto mide la diagonal mayor de tu rombo:")
diagonalMayor=float(input())
print("Ingresa cuanto mide la diagonal menor de tu rombo:")
diagonalMenor=float(input())
areaRombo=area_rombo(diagonalMayor,diagonalMenor)
print("El area del Rombo es:",areaRombo)




print("Ingresa cuanto mide base del triangulo:")
base=float(input())
print("Ingresa cuanto mide altura del triangulo:")
altura=float(input())
areaTriangulo=area_triangulo(base,altura)
print("El area del triánguloe es:",areaTriangulo)



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
    
   
