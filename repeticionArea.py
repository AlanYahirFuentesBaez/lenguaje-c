def area_triangulo(b,h):
    area=(b*h)/2
    return area



base=0
while(base <= 100):
    base=base+1
    if(base==101):
        break
    areaT=area_triangulo(base,10)
    print("La base mide:\t"+ str(base) + " la altura mide:10, el area es:\n\t" + str(areaT))


    
    
    #print("Quiere convertir a raiz cuadrada , presione 1 o a potencia cuadrada, presione 2")
    #pregunta = input()
    