# CIFRADO DE UN MENSAJE

# Cifrado César.
""" 
Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio César y sus tropas durante las Guerras 
Galas. La idea es bastante simple: cada letra del mensaje se reemplaza por su consecuente más cercano (A se 
convierte en B, B se convierte en C, y así sucesivamente). La única excepción es la Z, la cual se convierte en A.
"""

text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


