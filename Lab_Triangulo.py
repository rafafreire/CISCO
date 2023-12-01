'''
Ahora vamos a colocar la clase Point (ver Lab anterior) dentro de otra clase. Además, vamos a poner tres puntos en una clase, lo que nos permitirá definir un triángulo. ¿Cómo podemos hacerlo?

La nueva clase se llamará Triangle y esto es lo que queremos:

El constructor acepta tres argumentos - todos ellos son objetos de la clase Point.
Los puntos se almacenan dentro del objeto como una lista privada.
La clase proporciona un método sin parámetros llamado perimeter(), que calcula el perímetro del triángulo descrito por los tres puntos; el perímetro es la suma de todas las longitudes de los lados (lo mencionamos para que conste, aunque estamos seguros de que tú mismo lo conoces perfectamente).
Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la nuestra.

A continuación puedes copiar el código de la clase Point, el cual se utilizo en el laboratorio anterior:
'''
import math


class Point:
    #
    # El código del lab anterior.
    #
    def __init__(self, x=0.0, y=0.0):
        #
        # Escribir código aquí
        #
        self.__x = x
        self.__y = y

    def getx(self):
        #
        # Escribir código aquí
        #
        return self.__x

    def gety(self):
        #
        # Escribir código aquí
        #
        return self.__y

    def distance_from_xy(self, x, y):
        #
        # Escribir código aquí
        #
        dist_x = self.__x - x
        dist_y = self.__y - y
        #return math.hypot(math.sqrt((self.__x - x)**2 + (self.__y - y)**2))
        return math.hypot((self.__x - x) , (self.__y - y))


    def distance_from_point(self, point):
        #
        # Escribir código aquí
        #
        #return math.hypot(math.sqrt((self.__x - float(point.__x))**2 + (self.__y - float(point.__y))**2))
        #return math.hypot((self.__x - float(point.__x)), (self.__y - float(point.__y)))
        return self.distance_from_xy(point.getx(), point.gety())
    

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        # Escribir código aquí
        #
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        #
        # Escribir código aquí
        #
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i+1)%3])
        return per


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())


