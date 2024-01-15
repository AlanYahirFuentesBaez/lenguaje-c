def area_triangulo(b,h):
    area=(b*h)/2
    return area

def tablaMultiplicar(tabla):
    multiplicador=0
    while(multiplicador<9):        
        multiplicador=multiplicador+1
        resultado=tabla*multiplicador
        print("",tabla,"*",multiplicador,"resultado es: ",resultado)

def rectaNumerica(x):
    y=-pow(x,2)
    return y

for num in range(-100, 100, 3):
    print("Escribe el valor de entrada de la función:")
    entrada=num
    print("valor x=", entrada ,"valor y= ",rectaNumerica(entrada) )
    
    
print(tablaMultiplicar(100))

#numero=20
#while(numero<=20):
#    numero=numero+1
#    print(tablaMultiplicar(numero))

