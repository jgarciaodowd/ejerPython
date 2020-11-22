"""
# Un programa sinxelo, para calcular cadrados de números

print("Ejercicios 1.1 - 1.4 ")


def potencia():
    print("Calcularanse a potencia de dous números. ")
    n1 = input("Ingrese un número enteiro: ")
    n2 = input("Ingrese otro número enteiro: ")

    for x in range(int(n1), int(n2)):
        print(x * x)

    print("É todo por agora")


potencia()

# 1.5.1 Escribir un programa que pregunte o usuario: seu nome, e logo o saúde.

print("Ejercicio 1.5.1 ")

nombre = input("Introduzca su nombre: ")

print("Buenos días, " + nombre)


# 1.5.2 Escribir un programa que pregunte o usuario: dous números e logo mostre o produto.

print("Ejercicio 1.5.2 ")

num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))


def producto(a, b):
    producto = a * b
    print("El producto de ambos numeros es: " + str(producto))


producto(num1, num2)

# 1.6.1 Calcular o perímetro e área dun rectángulo dada sua base e sua altura.

base = int(input("Introduzca la base: "))
altura = int(input("Introduzca la altura: "))


def calcularPerimetroRectangulo(b, h):
    perimetro = 2 * b + 2 * h
    print("El perímetro es de: " + str(perimetro))


def calcularAreaRectangulo(b, h):
    area = b * h
    print("La base es de: " + str(area))

calcularPerimetroRectangulo(base, altura)
calcularAreaRectangulo(base, altura)

# 1.6.2 Calcular o perímetro e área dun círculo dado seu radio.


radio = int(input("Introduzca el radio: "))


def calcularPAC(r):
    import math
    perimetro = 2*math.pi * r
    area = math.pi * r**2

    print("El perímetro es de: " + str(perimetro))
    print("La base es de: " + str(area))

calcularPAC(radio)

# 1.6.3 Calcular o volume dunha esfera dado seu radio.


radio = int(input("Introduzca el radio: "))


def calcularVE(r):
    import math
    volumen = 4/3 * math.pi * r**3
    print("El volumen es de: " + str(volumen))

calcularVE(radio)

# 1.6.4 Calcular o área dun rectángulo (aliñado cos eixos x e y) dadas súas coordenadas x1, x2, y1, y2.

x1 = int(input("Introduzca un punto x: "))
x2 = int(input("Introduzca otro punto x: "))
y1 = int(input("Introduzca un punto y: "))
y2 = int(input("Introduzca otro punto y: "))


def calcularAR():
    base = 1
    altura = 2
    area = 3
    print()

calcularAR()

# 1.6.5 Dados os catetos dun triángulo rectángulo, calcular súa hipotenusa.

import math
cateto1 = int(input("Introduzca el cateto: "))
cateto2 = int(input("Introduzca otro cateto: "))


def calcularH(c1, c2):
    h = math.sqrt(cateto1**2 + cateto2**2)
    print("La hipotenusa es de: " + str(h))

calcularH(cateto1, cateto2)


# 1.1.8.1 Dados dous números, indicar a suma, resta, división e multiplicación de ambos.

numero1 = int(input("Introduzca el numero: "))
numero2 = int(input("Introduzca otro numero: "))


def operaciones(n1, n2):
    suma = n1 + n2
    resta = n1 - n2
    multi = n1 * n2
    divison = n1 / n2
    print("La suma de ambos numeros es de: " + str(suma))
    print("La resta de ambos numeros es de: " + str(resta))
    print("La multiplicación de ambos numeros es de: " + str(multi))
    print("La división de ambos numeros es de: " + str(divison))

operaciones(numero1, numero2)

# 1.1.8.2 Dado un número enteiro N, imprimir súa táboa de multiplicar.

num = int(input("Introduzca el numero: "))


def tabla(n):
    print("La tabla de multiplicar de " + str(n) + " es:")
    for i in range(1, 11):
        print(str(n) + "x" + str(i) + "= " + str(n * i))
tabla(num)

# 1.1.8.3 Dado un número enteiro N, imprimir seu factorial.

num = int(input("Introduzca el numero: "))


def factorial(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for j in range(1, n + 1):
            factorial = factorial * j
        return factorial


for i in num:
    print("El factorial de " + str(num[i]) + " es: " + str(factorial(num[i])))
factorial(num)


# 1.9. Escribir un programa que lle pida unha palabra o usuario,
# para logo imprimila 1000 veces, con espazos intermedios.

palabra = str(input("Escriba una palabra: "))


def reptirPalabra(p):
    for i in range(1000):
        print(str(p), end=" ")
reptirPalabra(palabra)


# 2.1.1 Escribir un ciclo definido para imprimir por pantalla tódolos números entre 10 e 20.


for i in range(10, 21):
    print(i)

# 2.1.2 Escribir un ciclo definido que saúde por pantalla os seus cinco mellores amigos/as.

mejoresAmigos = ["Alex", "Juan", "Pepe", "Luna", "Paula"]

for i in range(0, len(mejoresAmigos)):
    print("Hola, " + str(mejoresAmigos[i]))

# 2.1.3 Escribir un programa que use un ciclo definido con rango numérico,
# que pregunte os nomes dos seus cinco mellores amigos/as, e os saúde.

for i in range(5):
    nombre = str(input("Introduce un nombre: "))
    print("Buenos dias, " + nombre)

# 2.1.4 Escribir un programa que use un ciclo definido con rango numérico,
# que pregunte os nomes dos seus seis mellores amigos/as, e os saúde.

for i in range(6):
    nombre = str(input("Introduce un nombre: "))
    print("Buenos dias, " + nombre)


# 2.1.5 Escribir un programa que use un ciclo definido con rango numérico,
# que ache a cantos amigos queren saudar, lles pregunte os nomes de estes amigos/as, e os saúde.

amigos = int(input("Cuantos amigos quieres saludar? "))

for i in range(0, amigos):
    nombre = str(input("Como se llama tú amig@? "))
    print("Hola, " + str(nombre))


# 2.2. Escribir un programa que lle pregunte o usuario unha cantidade de pesos,
# una taxa de interese e un número de anos e mostre como resultado o monto final a obter

c = float(input("Cantidad de pesos? "))
x = float(input("Cual es la tasa de interés? "))
n = float(input("Durante cuantos años? "))

cn = c * (1 + x/100)**n

print("La cantidad total es: " + str(cn))


# 2.3. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
# Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

f = float(input("Que cantidad Fahrenheit quieres transformar a Celsius? "))

c = float(5 * (f - 32) / 9)

print("La temperatura en grados ºC es: " + str(c))


# 2.4. Utilice o programa anterior para xerar unha táboa de conversión de temperaturas,
# dende 0º F ata 120º F, de 10 en 10.


def ConvertirFaC(x):
    res = ((9 / 5) * x + 32)
    return res


def TablaF():
    for i in range(0, 130, 10):
        print(str(i) + " ºC = " + str(ConvertirFaC(i)) + " F")


TablaF()


# 2.5. Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario.

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)


# 2.6.1 Escribir un programa que reciba un número n por parámetro e
# imprima os primeiros n números triangulares, xunto co seu índice.

n = int(input("Introduce un numero: "))
acumulado = 0

for i in range(1, n + 1):
    acumulado = (acumulado + i)
    print(str(i) + " - " + str(acumulado))

# 2.6.2 Usando la ecuación n ∗ (n + 1) / 2.

n = int(input("Introduce un numero: "))

for i in range(1, n + 1):
    valor = i ∗ (i + 1) / 2
    print(str(i) + " - " + str(valor))



# 2.7. Escribir un programa que tome unha cantidade m de valores ingresados polo usuario,
# a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.

ERROR
def factorial(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for j in range(1, n + 1):
            factorial = factorial * j
        return factorial

m = int(input("Cuantos valores vas a introducir? "))
lista = []

for i in range(0, m):
    lista.append(input("Introduce el valor: "))

for x in range(0, len(lista)):
    fac = factorial(lista[x])
    print(str(x) + " - " + str(fac))


# 2.8. Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.


def fichasDomino():
    for i in range(0, 7):
        for j in range(i, 7):
            print(f'{i} : {j}')
fichasDomino()
"""
"""
# 2.9. Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.

n = int(input("Introduzca número máximo del dominó: "))
for i in range(n + 1):
    for j in range(i, n + 1):
        print(f'{i} : {j}')
"""