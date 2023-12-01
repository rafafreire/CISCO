## Pila

## Enfoque procedimental

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())



## POO

class Stack:
    def __init__(self):
        self.__stack_list = []
        print("Hola")

    def push(self, vale):
        self.__stack_list.append(vale)

    def pop(self):
        vale = self.__stack_list[-1]
        del self.__stack_list[-1]
        return vale


stack_object = Stack()
#print(len(stack_object.stack_list))

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())



class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self,vale):
        self.__sum += vale
        Stack.push(self, vale)

    def pop(self):
        vale = Stack.pop(self)
        self.__sum -= vale
        return vale
    
    def get_sum(self):
        return self.__sum
    

stack_object_adding = AddingStack()

for i in range(45):
    stack_object_adding.push(i)
print(stack_object_adding.get_sum())

for i in range (34):
    print(stack_object_adding.pop())


    

