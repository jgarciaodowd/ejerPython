"""
# 5.7.1. Escribir un programa que reciba una a una las notas del usuario,
# preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

nota = float(input("Introduzca la nota: "))


def promedioNotas(n):
    contador = 0
    suma = 0
    numero = 1

    while numero != 0:
        numero = int(input("Escribe otra nota (0 para terminar): "))

        if numero != 0:
            suma += numero
            contador += 1

    if contador == 0:
        print("No escribió ningún número. ")
    else:
        promedio = suma / contador
        print(f'El promedio es de {promedio}. ')

promedioNotas(nota)

"""
"""

# 5.7.2. Escribir una función que reciba un número entero k e imprima su descomposición en factores primos.

numero = int(input("Escribe un numero: "))


def factPrimos(k):
    i = 2
    print(1)
    while k >= i:
        if k % i == 0:
            print(i)
            k //= i
        else:
            i += 1
factPrimos(numero)


# 5.7.3.1 Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña,
# y no le permita continuar hasta que la haya ingresado correctamente.

contrasena = "contra"


def contra(con):
    while True:
        con = input("Contraseña: ")
        if con == contrasena:
            print("Contraseña correcta. ")
            break
        else:
            print("Contraseña incorrecta.")
contra(contrasena)


# 5.7.3.2 Modificar el programa anterior para que solamente permita una cantidad fija de intentos.

contrasena = "contra"


def contraIntentos(con):
    intentos = 3
    while intentos:
        con = input("Contraseña : ")
        if con == contrasena:
            print("Contraseña correcta. ")
            break
        else:
            print("Contraseña incorrecta. ")
            intentos -= 1
contraIntentos(contrasena)


# 5.7.3.3 Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor,
# utilizando la función sleep del módulo time.

from time import sleep
contrasena = "contra"


def contraConSleep(con):
    maxIntentos = 5
    intentos = maxIntentos
    while intentos != 0:
        con = input("Contraseña : ")
        if con == contrasena:
            print("Contraseña correcta. ")
            break
        else:
            print("Contraseña incorrecta. ")
            intentos -= 1
            if intentos > 0:
                sleep(10 - int(10 / maxIntentos * intentos))

contraConSleep(contrasena)
"""
"""
# 5.7.3.4 Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o
# no la contraseña correctamente, mediante un valor booleano (True o False).

from time import sleep
contrasena = "contra"


def contraConSleep(con):
    maxIntentos = 5
    intentos = maxIntentos
    while intentos != 0:
        con = input("Contraseña : ")
        if con == contrasena:
            print("Contraseña correcta. ")
            return True
            break
        else:
            print("Contraseña incorrecta. ")
            intentos -= 1
            if intentos > 0:
                sleep(10 - int(10 / maxIntentos * intentos))
    return False
contraConSleep(contrasena)

"""
"""
# 5.7.4. Utilizando la función randrange del módulo random, escribir un programa que obtenga un número aleatorio secreto
# y luego permita al usuario ingresar números y le indique sin son menores o
# mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.

from random import randrange

adivina = int(input("Adivina el número: "))
n = randrange(10)


def adivinarNum():
    if adivina == n:
        print("Has acertado el número! ")
    elif adivina < n:
        print("El número es más alto. ")
    else:
        print("El número es más bajo. ")
adivinarNum()



# 5.7.5 Implementar en python el algoritmo de Euclides para calcular el máximo común divisor de dos números n y m,
# dado por los siguientes pasos: 
# Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
# Si r es cero, n es el mcd de los valores iniciales.
# Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
# Hacer un seguimiento del algoritmo implementado para los siguientes pares de números: (15,9); (9,15); (10,8); (12,6).



def euclides(m, n):
    if m < n:
        cambio = m
        m = n
        n = cambio
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n
print(euclides(15, 9), euclides(9, 15), euclides(10, 8), euclides(12, 6))


# 5.7.6.1 Escribir una función es_potencia_de_dos que reciba como parámetro un número natural,
# y devuelva True si el número es una potencia de 2, y False en caso contrario.

num = int(input("Introduce un número natural: "))


def es_potencia_de_dos(n):
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            return False
    return True


es_potencia_de_dos(num)

# 5.7.6.2 Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las
# potencias de 2 que hay en el rango formado por esos números (0 si no hay ninguna potencia de 2 entre los dos).
# Utilizar la función es_potencia_de_dos, descripta en el punto anterior.

a = int(input("Introduce un número: "))
b = int(input("Introduce un número: "))


def suma_potencias_de_2(a, b):
    suma = 0
    for n in range(a, b + 1):
        if es_potencia_de_dos(n):
            suma += n
    print(str(suma))

suma_potencias_de_2(a, b)
"""
"""
# 5.7.7.1 Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.

num = int(input("Introduce un número: "))


def suma_divisores(n):
    suma = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            suma += i
    return suma
suma_divisores(num)

# 5.7.7.2 Usando la función anterior, escribir una función que imprima los primeros m números tales que la suma de sus
# divisores sea igual a sí mismo (es decir los primeros m números perfectos).

num = int(input("Introduce un número: "))


def perfecto(m):
    n = 1
    for i in range(m):
        while n != suma_divisores(n):
            n += 1
        print(n)
        n += 1


perfecto(num)

# 5.7.7.3 Usando la primera función, escribir una función que imprima las primeras m parejas de números (a,b),
# tales que la suma de los divisores de a es igual a b y
# la suma de los divisores de b es igual a a (es decir las primeras m parejas de números amigos).

num = int(input("Introduce un número: "))


def perfectos(m):
    a = 0
    for i in range(m):
        while True:
            a += 1
            b = suma_divisores(a)
            if suma_divisores(b) == a and a != b and a < b:
                print(a, b)
                break


perfectos(10)


# 5.7.8. Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales
# (primero uno, luego otro, y así hasta que el usuario ingrese -1 como condición de salida).
# Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

num = float(input("Introduzca un número: "))


def numNatu(n):
    i = 0
    total = 0
    while n == -1:
        if n != -1:
            n = float(input("Introduzca otro número: "))
            total += n
            i += 1
        else:
            promedio = total / i
            print("Se ingresaron" + str(i) + "números que suman" + str(total) + "y tienen de promedio" + str(promedio))

numNatu(num)


# 5.7.9.1 Escribir una función que reciba dos números como parámetros, 
# y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.
# Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))


def numMulFor(m,n):
     numMul = 0
     for i in range(m,n+1):
        if i % m == 0:
             numMul += 1
     print((str(numMul)))

numMulFor(num1, num2)

# 5.7.9.2 Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.

num = int(input("Introduce un número: "))
num1 = int(input("Introduce un número: "))


def num_mul(m,n):
    i=1
    mul = m
    while mul <= n:
         i += 1
         mul *= i
     print(str(i-1))
    
num_mul(num, num1)
"""
"""
# 5.7.10 Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.

num = int(input("Introduce un número: "))


def impNumPrimos(n):
    if n >= 2:
        print(2)
    for i in range(3, n + 1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)

impNumPrimos(num)

# 5.7.11 Escribir una función que reciba un dígito y un número natural,
# y decida numéricamente si el dígito se encuentra en la notación decimal del segundo.

digito = int(input("Introduce un dígito: "))
num = int(input("Introduce un número: "))


def digito(d, n):
    while n:
        if n % 10 == d:
            return True
        n = n // 10
    return False

digito()
"""

# 5.7.12 Escribir una función que dada la cantidad de ejercicios de un examen,
# y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen,
# revise un grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno,
# indicando con un valor centinela que no hay más examenes a revisar.
# Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos
# respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

ejer = int(input("Introduce número de ejercicios: "))
porcentaje = int(input("Introduce el porcentaje necesario para aprobar: "))


def examen(numEje, porcen):
    resueltos = float(input("Número de ejercicios resueltos (-1 para terminar): "))
    if resueltos == -1:
        return
    else:
        nota = 100 / numEje * resueltos
        print("El % de ejercicios resueltos es", 100 / numEje * resueltos)
        if nota < porcen:
            print("Suspendido")
        else:
            print("Aprobado")

examen(ejer, porcentaje)
