

class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def maullar(self):
        print("¡Miau!")
        
    def rasguña(self):
        print("¡Auuch!")


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def ladrar(self):
        print("¡Guau!")
    
    def morder(self):
        print("¡Arrrgh!")
        
p=Perro("Firulais",5)
p.ladrar()
p.morder()


g=Gato("Micifus",2)
g.maullar()
print(g.nombre)