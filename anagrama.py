str_1 = input("Ingresa la primera cadena: ")
str_2 = input("Ingresa la segunda cadena: ")

# Esto es lo que vamos a hacer con ambas cadenas:
# - quitar los espacios
# - cambiar todas las letras a mayúsculas
# - convertirlas en listas
# - ordenar las listas
# - unir los elementos de cada lista en cadenas separadas
# y finalmente, comparar ambas cadenas.
# ¡Hagámoslo!
str_1 = str_1.replace(" ", "").upper()
str_2 = str_2.replace(" ", "").upper()

list_1 = list(str_1)
list_2 = list(str_2)

list_1.sort()
list_2.sort()

string_1 = "".join(list_1)
string_2 = "".join(list_2)

print(string_1)
print(string_2)


if (string_1 == string_2):
    print("Es un anagrama")
else:
    print("No es un anagrama")



    