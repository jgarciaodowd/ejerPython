"""
# 3.1.1 Calcular a cantidade de segundos nun tempo dado en horas, minutos e segundos.

hor = int(input("Introduce la cantidad de tiempo en horas: "))
min = int(input("Introduce la cantidad de tiempo en minutos: "))
seg = int(input("Introduce la cantidad de tiempo en segundos: "))


def HMSToSeg(h, m, s):
    t = ((h * 60) + m) * 60 + s
    print("El tiempo total en segundos es de: " + str(t))


HMSToSeg(hor, min, seg)


# 3.1.2 Calcular a cantidade de horas, minutos e segundos dun tempo dado en segundos.

seg = int(input("Introduce la cantidad de tiempo en segundos: "))


def SegToHMS(s):
    horas = int(s // 3600)
    s = int(s % 3600)
    minutos = int(s // 60)
    segundos = int(s % 60)
    print("El tiempo total en horas, minutos y segundos es de: " + str(horas) + " h " + str(minutos) + " min "
          + str(segundos) + " s")


SegToHMS(seg)


# 3.2. Usando as funcións do exercicio anterior, escribir un programa que lea de teclado dous tempos expresados en horas
# minutos e segundos; as sume e mostre o resultado en horas, minutos e segundos por pantalla.

h1 = int(input("Introduce horas    1: "))
m1 = int(input("Introduce minutos  1: "))
s1 = int(input("Introduce segundos 1: "))
h2 = int(input("Introduce horas    2: "))
m2 = int(input("Introduce minutos  2: "))
s2 = int(input("Introduce segundos 2: "))

t = int(SegToHMS(HMSToSeg(h1, m1, s1)) + int(HMSToSeg(h2, m2, s2)))

print()


# 3.3. Escribir unha función que dados catro números, devuelte o maior producto de dous de elles. Por exemplo,
# si recibe os números 1, 5, -2, -4 debe devoltar 8, que é o producto máis grande que se pode obter entre eles.

num1 = int(input("Introduce número 1 : "))
num2 = int(input("Introduce número 2 : "))
num3 = int(input("Introduce número 3 : "))
num4 = int(input("Introduce número 4 : "))


def mayor_producto(n1, n2, n3, n4):
    mayor = n1 * n2
    n1n3 = n1 * n3
    n1n4 = n1 * n4
    n2n3 = n2 * n3
    n2n4 = n2 * n4
    n3n4 = n3 * n4
    if n1n3 > mayor:
        mayor = n1n3
    elif n1n4 > mayor:
        mayor = n1n4
    if n2n3 > mayor:
        mayor = n2n3
    elif n2n4 > mayor:
        mayor = n2n4
    if n3n4 > mayor:
        mayor = n3n4
    print("El mayor producto entre ellos es: " + str(mayor))

mayor_producto(num1, num2, num3, num4)


# 3.4.1) Escribir uhna función que dado un vector o orixen (definido polos seus puntos x, y),
# devuelte a norma do vector, dada por (x^2 + y^2) ^ 1/2

x = int(input("Introduce la cordenada x: "))
y = int(input("Introduce la cordenada y: "))


def norma(x, y):
    n = (x**2 + y**2)**(1/2)
    print("La norma es igual a: " + str(n))
norma(x, y)


# 3.4.2) Escribir unha función que dados dous puntos no plano (x1, y1 y x2, y2),
# devuelte a resta de ambos (debe devoltar un par de valores).

x1 = int(input("Introduce la cordenada x1: "))
y1 = int(input("Introduce la cordenada y1: "))
x2 = int(input("Introduce la cordenada x2: "))
y2 = int(input("Introduce la cordenada y2: "))


def resta(x1, y1, x2, y2):
    r = x1 - x2, y1 - y2
    print("La rsta de ambos es: " + str(r))
resta(x1, y1, x2, y2)



# 3.4.3) Utilizando as funcións anteriores, escribir unha función que dados dous puntos no plano (x1, y1 y x2, y2),
# devuelte a distancia entre ambos.

x1 = int(input("Introduce la cordenada x1: "))
y1 = int(input("Introduce la cordenada y1: "))
x2 = int(input("Introduce la cordenada x2: "))
y2 = int(input("Introduce la cordenada y2: "))


def distancia(x1, y1, x2, y2):
    (x, y) = resta(x1, y1, x2, y2)
    d = norma(x, y)
    if d < 0:
        d = -d
    print("La distancia entre ambos es de: " + str(d))
distancia(x1, y1, x2, y2)


# 3.4.4) Escribir unha función que reciba un vector o orixe (definido polos seus puntos x, y) e
# devuelte un vector equivalente, normalizado (debe devoltar un par de valores).

x = int(input("Introduce la cordenada x: "))
y = int(input("Introduce la cordenada y: "))


def vector_unitario(x, y):
    n = (x**2 + y**2)**(1/2)
    normalizado = x / n, y / n
    print("El vector equivalente normalizado es: " + str(normalizado))
vector_unitario(x, y)


# 3.4.5) Utilizando as funciones anteriores (b e d), escribir unha función que dados dous puntos no plano
# (x1, y1 y x2, y2), devuelte o vector dirección unitario correspondiente a recta que os une.

x1 = int(input("Introduce la cordenada x1: "))
y1 = int(input("Introduce la cordenada y1: "))
x2 = int(input("Introduce la cordenada x2: "))
y2 = int(input("Introduce la cordenada y2: "))


def vector_unitario2(x1, y1, x2, y2):
    (x, y) = resta(x2, y2, x1, y1)
    print("El vector dirección unitario es: " + str(vector_unitario(x, y)))

vector_unitario2(x1, y1, x2, y2)
"""
"""
# 3.4.6) Escribir unha función que reciba un punto (x, y), unha dirección unitaria dunha recta (dx, dy)
# e un punto pertenecente a esa recta (cx, cy) e devuelte a proxección do punto sobre a recta.

x = int(input("Introduce la cordenada x: "))
y = int(input("Introduce la cordenada y: "))
dx = int(input("Introduce la cordenada dx: "))
dy = int(input("Introduce la cordenada dy: "))
cx = int(input("Introduce la cordenada cx: "))
cy = int(input("Introduce la cordenada cy: "))


def proyeccion(x, y, dx, dy, cx, cy):
    (t1, t2) = resta(x, y, cx, cy)
    p11 = dx*dx
    p12 = dx*dy
    p21 = p12
    p22 = dy*dy
    rx = p11 * t1 + p12 * t2
    ry = p21 * t1 + p22 * t2
    rx += cx
    ry += cy
    print(str(rx, ry))

proyeccion(x, y, dx, dy, cx, cy)


# 3.4.7)  Escribir unha función que calcule o área dun triángulo a partir da súa base e a súa altura.

base = int(input("Introduce la base: "))
altura = int(input("Introduce la altura: "))


def area_triangulo(b, h):
    area = b*h/2
    print("El área del triángulo es: " + str(area))
area_triangulo(base, altura)


# 3.4.8) Utilizando as funcións anteriores escribir unha función que reciba tres puntos no
# plano (x1, y1, x2, y2 y x3, y3) e devolte o área do triángulo correspondente.

x1 = int(input("Introduce la cordenada x1: "))
y1 = int(input("Introduce la cordenada y1: "))
x2 = int(input("Introduce la cordenada x2: "))
y2 = int(input("Introduce la cordenada y2: "))
x3 = int(input("Introduce la cordenada x3: "))
y3 = int(input("Introduce la cordenada y3: "))


def area_vectorial(x1, y1, x2, y2, x3, y3):
    (dos_uno_x, dos_uno_y) = resta(x2, y2, x1, y1)
    (dos_tres_x, dos_tres_y) = resta(x3, y3, x1, y1)
    area = dos_uno_x * dos_tres_y - dos_uno_y * dos_tres_x
    if area < 0:
        area = -area
    print("El área vectorial es de: " + str(area / 2))
area_vectorial(x1, y1, x2, y2, x3, y3)


def areaTriangulo(x1, y1, x2, y2, x3, y3):
    base = distancia(x1, y1, x3, y3)
    (dx, dy) = vector_unitario2(x1, y1, x3, y3)
    (px, py) = proyeccion(x2, y2, dx, dy, x3, y3)
    altura = distancia(x2, y2, px, py)
    print("El área del triángulo es: " + str(area_triangulo(base, altura)))
    
areaTriangulo(x1, y1, x2, y2, x3, y3)
"""

# 4.1. Debemos leer un número y, si el número es positivo, debemos escribir en pantalla el cartel "Numero positivo".

numero = int(input("Introduzca un número entero: "))


def compPositivo():
    if numero > 0:
        print("Número positivo. ")
    elif numero == 0:
        print("El número es igual a cero. ")
    else:
        print("Número negativo. ")
compPositivo()
