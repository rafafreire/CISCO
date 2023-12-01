# Vamos a operar con cadenas


'alpha' == 'alpha'
'alpha' != 'Alpha'

'alpha' < 'alphabet'

'beta' > 'Beta'

'10' == '010'
'10' > '010'
'10' > '8'
'20' < '8'
'20' < '80'

# No se pueden comparar cadenas y enteros porque da error
"""
'10' == 10
'10' != 10
'10' == 1
'10' != 1
'10' > 10

"""


# Ordenamiento

greek = ['omega', 'alpha', 'pi', 'gamma']

# Demostración de la función sorted():
# El método sorted devuelve una nueva lista ordenada  
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()


# Demostración del método sort():
# El método sort ordena la lista que llama
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)


# Conversión de un número a un string con str()
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)


# Conversión de un string a un entero (int) o un flotante (float)

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)


# Ejemplos 1
print('smith' > 'Smith')
print('Smiths' < 'Smith')
print('Smith' > '1000')
print('11' < '8')

# Ejemplos 2

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])

# Ejemplo 3
"""
s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)
"""



# Ejemplos de 7 segmentos

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

# para crear el dígito
segse = [ [' ',' ',' '] for lin in range(5) ]
print(segse)

def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Ingresa el número que deseas mostrar: ")))