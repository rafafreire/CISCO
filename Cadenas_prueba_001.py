str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

print(ord(str1)) # Muestra el orden del caracter en el codigo ascii
print(chr(97)) # Muestra el caracter del codigo ascii pasandole el numero de orden 

print (ord(chr(97)) == 97)
print(chr(ord('a')) == 'a')
print(chr(ord(str1)) == str1 )

the_string = "Stranger Things"

for it in range(len(the_string)):
    print(the_string[it], end = " ")
print ()

for caracter in the_string:
    print(caracter, end = "  ")
print()

# Rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# In y not in
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet) # f está en el alfabeto
print("F" in alphabet) # F no está en el alfabeto
print("1" in alphabet) # 1 no está en el alfabeto
print("ghi" in alphabet) # ghi está en el alfabeto

print()
print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


# Las cadenas son inmutables (no se pueden cambiar)
alphabet = "abcdefghijklmnopqrstuvwxyz"
# del alphabet[0]

# alphabet.append("A") # Las cadenas no tienen el atributo append

# alphabet.insert(0, "A") # Las cadenas no tienen el atributo insert

alphabet = "bcdefghijklmnopqrstuvwxy"
print (alphabet)

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

# Utilizamos la función min para devolver el primer caracter de la tabla ASCII
# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ"))

# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))


# Demostración de max() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# El método index devuelve el lugar de la cadena donde aparece la primera ocurrencia y si no la encuentra da un error
# Demonstración del método index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
# print("aAbByYzZaA".index("p")) # nos muestra el error por no haber encontrado la letra

# La función list crea una nueva lista a partir de una cadena
# Demostración de la función list():
print(list("abcabc"))


# el método count() cuenta el numero de veces que se repite un caracter o cadena
# Demostración del método count():
print("abcabc".count("b"))
print('abcabc'.count("d"))
print("abcabc".count("bc"))

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)

for charact in "abc":
    print(chr(ord(charact) + 1), end=' ')






