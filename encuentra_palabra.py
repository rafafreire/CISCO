word = input("Ingresa la palabra que deseas encontrar: ").upper()
strn = input("Ingresa la cadena en donde deseas buscar: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Si")
else:
	print("No")