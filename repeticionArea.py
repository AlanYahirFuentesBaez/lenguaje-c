def area_triangulo(b,h):
    area=(b*h)/2
    return area

def tablaMultiplicar(tabla):
    multiplicador=0
    while(multiplicador<10):        
        multiplicador=multiplicador+1
        resultado=tabla*multiplicador
        print("",tabla,"*",multiplicador,"resultado es: ",resultado)
        
numero=20
while(numero<=20):
    numero=numero+1
    print(tablaMultiplicar(numero))
