'''
Necesitamos una clase capaz de contar segundos. ¿Fácil? No es tan fácil como podrías pensar, ya que tendremos algunos requisitos específicos.

Léelos con atención, ya que la clase sobre la que escribes se utilizará para lanzar cohetes en misiones internacionales a Marte. Es una gran responsabilidad. ¡Contamos contigo!

Tu clase se llamará Timer (temporizador en español). Su constructor acepta tres argumentos que representan horas (un valor del rango [0..23]; usaremos tiempo militar), minutos (del rango [0. .59]) y segundos (del rango [0..59]).

Cero es el valor predeterminado para todos los parámetros anteriores. No es necesario realizar ninguna comprobación de validación.

La clase en sí debería proporcionar las siguientes facilidades:

Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la siguiente forma: "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera de los valores es menor que 10.
La clase debe estar equipada con métodos sin parámetros llamados next_second() y previous_second(), incrementando el tiempo almacenado dentro de los objetos en +1/-1 segundos respectivamente.
Emplea las siguientes sugerencias:

Todas las propiedades del objeto deben ser privadas.
Considera escribir una función separada (¡no un método!) para formatear la cadena con el tiempo.
Completa la plantilla que te proporcionamos en el editor. Ejecuta tu código y comprueba si el resultado es el mismo que el nuestro.

'''

class Timer:
    def __init__(self, horas, minutos, segundos ):
        #
        # Escribir código aquí
        #
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def two_digits(self, val):
        s = str(val)
        if len(s) == 1:
            s = '0' + s
        return s

    def __str__(self):
        #
        # Escribir código aquí
        #
        return self.two_digits(self.horas) + ":" + self.two_digits(self.minutos) + ":" + self.two_digits(self.segundos)

    def next_second(self):
        #
        # Escribir código aquí
        #
        if (self.segundos + 1 == 60):
            self.segundos = 0
            self.minutos += 1
            if (self.minutos == 60):
                self.minutos = 0
                self.horas += 1
                if (self.horas == 24):
                    self.horas = 0

    def prev_second(self):
        #
        # Escribir código aquí
        #
        if (self.segundos - 1 == -1):
            self.segundos = 59
            self.minutos -= 1
            if (self.minutos == -1):
                self.minutos = 59
                self.horas -= 1
                if (self.horas == -1):
                    self.horas = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    

