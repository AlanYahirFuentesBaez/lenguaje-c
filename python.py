numero = float(input('Ingresa el número de personas a registrar:'))

while(numero > 0):
    numero=numero-1
    nombre=input('ingresa el nombre: ')
    edad=input('Ingresa la edad: ' )
    curp=input('Ingresa el curp: ')
    print(nombre+edad+curp)
    print('Ingresa la siguiente persona')

print('Has terminado de ingresar las personas.')

