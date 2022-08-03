#El import es la 
import math
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class persona:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura


persona=persona("Juan", 20, 70, 1.70)

print(persona)
root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.left.left = Node(5)
root.left.right = Node(50)
   
print (root)
print (root.left.left.left.data)