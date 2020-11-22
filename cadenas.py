cadena1 = input("Escribe una cadena: ")
"""
# 6.1.1 Imprima os dous primeiros caracteres.

print(cadena1[:2])

# 6.1.2 Imprima os tres últimos caracteres.

print(cadena1[:-4:-1])

# 6.1.3 Imprima dita cadena cada dous caracteres. Ex.: recta debería imprimir rca

print(cadena1[::2])

# 6.1.4 Dita cadea en sentido inverso. Ex.: Ola mundo! debe imprimir !odnum alO

print(cadena1[::-1])

# 6.1.5 Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer.

print(cadena1 + cadena1[::-1])

# 6.2.1 Inserte o caracter entre cada letra da cadea. Ex: separar, debería devoltar s,e,p,a,r,a,r

for i in range(0, len(cadena1) - 1):
    print(cadena1[i], end=",")
print(cadena1[:-2:-1])


# 6.2.2 Reemplace tódolos espacios polo caracter.
# Ex: meu arquivo de texto.txt e ‘\_’ ç debería devoltar meu\_arquivo\_de\_texto.txt

for i in range(0, len(cadena1) - 1):
    print(cadena1[i].replace(" ", "\_"), end="")
print(cadena1[:-2:-1])

# 6.2.3 Reemplace tódolos díxitos n a cadea polo caracter.
# Ex: Súa clave é: 1540 e ‘X’, debería devoltar Súa clave é: XXXX

for i in range(0, len(cadena1)):
    print(cadena1[i].replace((cadena1[i]), "X"), end="")


# 6.2.4 Inserte o caracter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0

contador = 0
for i in range(0, len(cadena1)):
    print(cadena1[i], end="")
    contador = contador + 1
    if contador == 3:
        print(".", end="")
        contador = 0

# 6.3. Modificar las funciones anteriores, para que reciban un parámetro que indique la cantidad máxima de reemplazos o
# inserciones a realizar.


def insertarCarc1(num):
    cont = 0
    for i in range(0, len(cadena1) - 1):
        print(cadena1[i], end=",")
        cont += 1
        if cont == num:
            j = i + 1
            for j in range(j, len(cadena1) - 1):
                print(cadena1[j], end="")
            break
    print(cadena1[:-2:-1])

insertarCarc1(4)



def insertarCarac2(num):
    cont = 0
    for i in range(0, len(cadena1) - 1):
        print(cadena1[i].replace(" ", "\_"), end="")
        cont += 1
        if cont == num:
            j = i + 1
            for j in range(j, len(cadena1) - 1):
                print(cadena1[j], end="")
            break
    print(cadena1[:-2:-1])

insertarCarac2(1)
"""

"""
def insertarCarc3(num):
    cont = 0
    for i in range(0, len(cadena1)):
        print(cadena1[i].replace((cadena1[i]), "X"), end="")
        cont += 1
        if cont == num:
            j = i + 1
            for j in range(j, len(cadena1)):
                print(cadena1[j], end="")
            break

insertarCarc3(4)


def insertarCarc4(num):
    contador = 0
    cont_puntos = 0
    for i in range(0, len(cadena1)):
        print(cadena1[i], end="")
        contador += 1
        cont_puntos += 1
        if contador == 3:
            print(".", end="")
            contador = 0
        if cont_puntos == num + 1:
            j = i + 1
            for j in range(j, len(cadena1)):
                print(cadena1[j], end="")
            break
insertarCarc4(2)
"""
"""
# 6.4. Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena
# con el número y las separaciones de miles. Por ejemplo, si recibe 1234567890, debe devolver 1.234.567.890.

cad2 = ""
cont = 1
for caracter in cadena1[::-1]:
    cad2 = caracter + cad2
    if cont % 3 == 0:
        cad2 = "." + cad2
    cont = cont + 1
print(cad2)



# 6.5.1 La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.

def primeraLetra():
    palabras = cadena1.split()
    nueva_cadena = ""
    for palabra in palabras:
        nueva_cadena = nueva_cadena + str(palabra[0])
    print(nueva_cadena)


primeraLetra()

# 6.5.2 Dicha cadena con la primera letra de cada palabra en mayúsculas.
# Por ejemplo, si recibe república argentina debe devolver República Argentina.

for palabra in cadena1:
    print(palabra.capitalize(), end=" ")

# 6.5.3 Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.

for palabra in cadena1:
    if palabra.startswith("a") or palabra.startswith("A"):
        print(palabra, end=" ")


# 6.6.1 Devuelva solamente las letras consonantes. Por ejemplo, si recibe algoritmos o logaritmos debe devolver lgrtms.


def devolverConso(cadena):
    nueva_cadena = ""
    list = ("a", "e", "i", "o", "u")
    cadena.lower()
    for letra in list:
        cadena = cadena.replace(letra, "")
    print(cadena)

devolverConso(cadena1)

# 6.6.2 Devuelva solamente las letras vocales. Por ejemplo, si recibe sin consonantes debe devolver i ooae.

def devolverVocales(cadena):
    nueva_cadena = ""
    list = (
        "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
    cadena.lower()
    for letra in list:
        cadena = cadena.replace(letra, "")
    print(cadena)

devolverVocales(cadena1)

# 6.6.3 Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe vestuario debe devolver vistaerou.


def vocalPorVocal(cadena):
    nueva_cadena = ""
    voc = "aeiouAEIOU"
    for i in cadena:
        if i in "aeiou":
            nueva_cadena += voc[voc.find(i)+1]
        else:
            nueva_cadena += i
    print(nueva_cadena)

vocalPorVocal(cadena1)
"""
"""
# 6.6.4Indique si se trata de un palíndromo. Por ejemplo, anita lava la tina es un palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda).


def esPalindromo(cadena):
    cad_limpia = ""
    for i in cadena:
        if i != " ":
            cad_limpia += i
    if cad_limpia == cad_limpia[::-1]:
        print("Es un palíndromo. ")
    else:
        print("No es un palíndromo. ")

esPalindromo(cadena1)

# 6.7.1 Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.

cadena2 = str(input("Escriba otra cadena: "))


def subcadena(cad1, cad2):
    if cad1.find(cad2) != -1:
        print("Es una subcadena de la primera. ")
    else:
        print("No es una subcadena de la primera. ")
subcadena(cadena1, cadena2)


# 6.7.2 Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe kde y gnome debe devolver gnome.

cadena2 = input("Introduce otra palabra: ")


def comprobarOrden():
    cadenas = [cadena1, cadena2]
    print("La cadena mas pequeña es: " + min(cadenas))

comprobarOrden()
"""

#  6.8 Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria)
#  y devuelva el valor decimal correspondiente.


def binADecimal(num):
    dec = 0
    for i in num:
        dec *= 2
        if i == "1":
            dec += 1
    print("Esta representación binaria: " + num + " corresponde a este número decimal: " + str(dec))

binADecimal(cadena1)
