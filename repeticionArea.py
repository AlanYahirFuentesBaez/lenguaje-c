def area_triangulo(b,h):
    area=(b*h)/2
    return area

def tablaMultiplicar(tabla):
    multiplicador=0
    while(multiplicador<9):        
        multiplicador=multiplicador+1
        resultado=tabla*multiplicador
        print("",tabla,"*",multiplicador,"resultado es: ",resultado)
        
<<<<<<< HEAD
numero=9
while(numero<10):
=======
numero=20
while(numero<=20):
>>>>>>> python
    numero=numero+1
    print(tablaMultiplicar(numero))
