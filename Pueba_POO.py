class A:
    def __init__(self):
        self.a = 1
 
 
class B(A):
    def __init__(self):
        A.__init__(self)
        # Colocar la línea seleccionada aquí.
        self.b = 2


