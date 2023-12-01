"""
1. Algunos de los métodos que ofrecen las cadenas son:

capitalize(): cambia todas las letras de la cadena a mayúsculas.
center(): centra la cadena dentro de una longitud conocida.
count(): cuenta las ocurrencias de un carácter dado.
join(): une todos los elementos de una tupla/lista en una cadena.
lower(): convierte todas las letras de la cadena en minúsculas.
lstrip(): elimina los caracteres en blanco al principio de la cadena.
replace(): reemplaza una subcadena dada con otra.
rfind(): encuentra una subcadena comenzando por el final de la cadena.
rstrip(): elimina los caracteres en blanco al final de la cadena.
split(): divide la cadena en una subcadena usando un delimitador dado.
strip(): elimina los espacios en blanco iniciales y finales.
swapcase(): intercambia las mayúsculas y minúsculas de las letras.
title(): hace que la primera letra de cada palabra sea mayúscula.
upper(): convierte todas las letras de la cadena en mayúsculas.

2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

endswith(): ¿La cadena termina con una subcadena determinada?
isalnum(): ¿La cadena consta solo de letras y dígitos?
isalpha(): ¿La cadena consta solo de letras?
islower(): ¿La cadena consta solo de letras minúsculas?
isspace(): ¿La cadena consta solo de espacios en blanco?
isupper(): ¿La cadena consta solo de letras mayúsculas?
startswith(): ¿La cadena consta solo de letras mayúsculas?


"""


cadena = "aBcD"

# Metodos de las cadenas en python

# Método capitalize()
print("Cadena: " + cadena)
print("Cambio capitalize: " + cadena.capitalize())

# Ejemplos:

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# Método center():
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')


# Método center con dos atributos
print('[' + 'gamma'.center(20, '*') + ']')


# Método endswith()

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")


t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Método find()
# Demostración del método find():
# El método find busca unos carateres dentro de la cadena y devuelve la posición
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))


the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)



print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))


# Demostración del método isalnum():
# El metodo isalnum comprueba si la cadena es con datos alfanuméricos
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

# Ejemplo: Demostración del método isalpha():
# El método isalpha se centra solamente en letras y devuelve True o False 
print("Moooo".isalpha())
print('Mu40'.isalpha())


# Ejemplo: Demostración del método isdigit():
# El método isdigit comprueba si la cadena son solo digitos
print('2018'.isdigit())
print("Year2019".isdigit())


# Ejemplo: Demostración del método islower():
# El método islower comprueba si todas las letras son minúsculas
print("Moooo".islower())
print('moooo'.islower())


# Ejemplo: Demostración del método isspace():
# El método isspace() identifica los espacios en blanco
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())


# Ejemplo: Demostración del método isupper():
# El método isupper identifica que todas las letras estén en mayusculas
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


# Demostración del método join():
# El método join junta los datos que se le pasan con la cadena principal
print(",".join(["omicron", "pi", "rho"]))

# Demostración del método lower():
# El método lower cambia las letras MAYUSCULAS a minúsculas
print("SiGmA=60".lower())

# Demostración del método lstrip():
# El método lstrip() devuelve una cadena eliminando todos los espacios en blanco iniciales
print("[" + " tau ".lstrip() + "]")

# Si se le pasa un caracter se eliminara todos los caracteres antes de ese caracter (incluidos)
print("www.cisco.com".lstrip("w."))

print("pythoninstitute.org".lstrip(".org"))


# Demostración del método replace():
# El método replace cambia caracteres o cadenas si coinciden con el señuelo
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))


# Si le pasamos tres parámetros el tercero nos limita el número de reemplazos
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))


# Demostración del método rfind():
# El método rfind hace lo mismo que find pero comenzando por el final
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demostración del método rstrip():
# El método rstrip elimina todos los espacios en blanco por la derecha
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demostración del método split():
# El método split extrae en una lista todas las cadenas que están separadas con un espacio en blanco (inversa de join())
print("phi       chi\npsi".split())


# Demostración del método startswith():
# El método startswith() comprueba si una cadena comienza con una subcadena especificada
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demostración del método strip():
# El método strip() devuelve una cadena eliminando todos los espacios en blanco
print("[" + "   aleph   ".strip() + "]")


# Demostración del método swapcase():
# El método swapcase() cambia los caracteres en minuscula a MAYUSCULA y los que están en MAYUSCULA a minuscula
print("Yo solo sé que no sé nada".swapcase())

print()

    
# Demostración del método title():
# El método title() cambia la primera letra de cada palabra a Mayúscula y las demás a minúsculas
print("Yo solo sé que no sé nada. Parte 1.".title())

print()

# Demostración del método upper():
# El método upper cambia todas los caracteres a MAYUSCULAS
print("Yo solo sé que no sé nada. Parte 2.".upper())





# Ejemplo 1

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

print("")


# Ejemplo 2

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
print(s2[-2])


# Ejemplo 3

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s)


# Ejemplo 4

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)






