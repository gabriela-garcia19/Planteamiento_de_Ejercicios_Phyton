"""1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros números de la serie de Fibonacci."""
"""0,1,1,2,3,5,8,13,21,34,55..."""

numero = int(input("Hasta donde se genera la sucesion de Fibonacci: "))
n1 = 0
n2 = 1
print(n1)
print(n2)

for i in range(numero - 2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

"""2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores"""


def divisores(numero):
    resultado = [i for i in range(1, numero + 1) if numero % i == 0]
    return resultado


print("los divisores del numero son:", divisores(8))

"""3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original."""


def buy(list, budget):
    print(f"mi lista a comprar: {list} | presupuesto {budget}")


buy(["arroz", "harina", "huevos"], 50)

"""4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos."""


def sumar_digitos(cadena):
    suma = 0
    for i in cadena:
        suma += int(i)
    return suma


numero = input("Ingresa un numero: ")
print(f"la suma de los digitos de los numeros es: {sumar_digitos(numero)}")

"""5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena."""


def obtener_vocales(frase):
    vocales = "aeiouAEIOU"
    return [c for c in frase if c in vocales]


texto = input("Ingresa un texto: ")
print(f"la suma de las vocales de la cadena es: {len(obtener_vocales(texto))}")

"""6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
"""

lista = [
    "hola",
    "profesor",
    "este es mi ejercicio",
    6,
    "de phyton",
    "espero este codigo",
    "cumpla los requisitos",
]
print(f"los primeros 4 elementos de la lista son: {(lista[0:4])}")

"""7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
"""


def contador_minusculas_mayusculas(cadena):
    contador = {"minusculas": 0, "mayusculas": 0}
    for c in cadena:
        if c.isupper():
            contador["mayusculas"] += 1
        elif c.islower():
            contador["minusculas"] += 1
    return contador


frase = input("Ingresa un texto: ")
print(f"la cantidad de letras es: {(contador_minusculas_mayusculas(frase))}")

"""8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3."""


def es_numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero


print(f"El numero es: {(es_numero_perfecto(6))}")

"""9. Ejercicio: Define una función que reciba un número y retorne su representación en binario."""

numero = 10
print(f"El numero binario es: {(bin(numero))}")

"""10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas)."""


def elementos_comunes(lista_1, lista_2):
    conjunto_1 = set(lista_1)
    conjunto_2 = set(lista_2)

    return list(conjunto_1 & conjunto_2)


numeros_1 = [3, 4, 6, 7, 2, 5]
numeros_2 = [4, 1, 0, 2, 9]

resultado = elementos_comunes(numeros_1, numeros_2)

print(f"los numeros comunes son: {(resultado)}")

"""11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""


def es_palindromo(cadena):
    posicion_izquierda = 0
    posicion_derecha = len(cadena) - 1
    while posicion_derecha >= posicion_izquierda:
        if not cadena[posicion_izquierda] == cadena[posicion_derecha]:
            return False

        posicion_izquierda += 1
        posicion_derecha -= 1
    return True

print(f"¿La cadena es palindromo?: {(es_palindromo("oso"))}")

''' 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”. '''

for n in range(1, 50):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

'''13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.'''

mi_lista = [7, 12, 9, 10, 150]
mi_lista.sort()
print("Mi lista Ordenadaes: ", mi_lista)

'''14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
'''
def encontrar_palabra_mas_larga(palabras):
    palabra_longitud = []

    for p in palabras:
        palabra_longitud.append((len(p), p))
    palabra_longitud.sort()
    return palabra_longitud [-1][1]

palabras = ['videojuegos', 'phyton', "1234", "ordenador"]
print(f"La palabra mas larga es: {(encontrar_palabra_mas_larga(palabras))}")

'''15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.'''
numero = int(input("Ingrese un numero para calcular la serie de Fibonacci: "))
n1 = 0
n2 = 1
print(n1)
print(n2)

for i in range(numero - 2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

'''16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista'''

def maximo_lista(numeros):
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo
mi_lista = [10, 12, 6, 1, 33]
print(f"El numero mas grande de mi lista es: {(maximo_lista(mi_lista))}")

'''17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.'''

num = int (input("Ingrese un numero de maximo 4 cifras:"))
if num >= 0 and num <= 9999:
    numT = str (num)
    suma = int (numT[0]) + int(numT[1]) + int(numT[2]) + int(numT[3])
    cuadrado = suma * suma
    print ("la suma es: ", suma)
    print ("el cuadrado de la suma es:" ,cuadrado)
else:
    print("Debe ingresar un numero de 4 cifras")

'''18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.'''

def segundo_mayor(numeros):
    if isinstance (numeros, list):
        if len(numeros) < 2:
            return None
        
    if len (numeros) == 2 and numeros [0]== numeros == [1]:
        return None
    
    duplicados = set ()
    unicos = []

    for n in numeros:
        if n not in duplicados:
            duplicados.add(n)
            unicos.append(n)

    unicos.sort()
    return unicos [-2]

numeros =[1, 5,7 ,90, 5, 55, 78, 12]

print(f"El segundo numero mas grande de mi lista es: {(segundo_mayor(numeros))}")

'''19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.'''

l1 = [1, 13, 11, 5, 7, 19]
l2 = [15, 7, 9, 8, 4]

def superposicion (a,b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False
print (superposicion (l1,l2))

'''20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.'''

lista = [4, 1, 78, 34, 65]
lista_invertida = lista[::-1]
print(f"Mi lista en el orden inverso es: {(lista_invertida)}")

'''21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.'''

def contar_digitos_letras(cadena):
    digitos = 0
    letras = 0

    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
        
    return digitos, letras
texto = input ('Escriba un texto: ')
resultado = contar_digitos_letras(texto)

print ('La cantidad de digitos: %i' % resultado [0])
print ('La candidad de letras: %i' % resultado [1])

'''22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números'''

def sumar_lista(lista):
    suma = 0

    for numero in lista:
        suma += numero
    return suma

numeros = [1, 2, 6, 3, 5]

print (f"La suma de los numeros de la lista es: {(sumar_lista(numeros))}")

'''23. Ejercicio: Define una función que encuentre el elemento más común en una lista.'''

from collections import Counter

a = [1,1,2,1,3,7,9,5]
counter = Counter(a)

first, second, *_, last = counter.most_common()

print(f"A continuacion se muestra el elemento mas comun y el numero de repeticiones en la lista: {(first)}")

'''24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.'''

numero = int(input('Escriba un numero entero: '))
for i in range (1, 11):
    print (f'{i} x {numero} = {i * numero}')
    
'''25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.'''

from collections import Counter, defaultdict
frase = "Aprendiendo Phyton"
resultado = {}
for c in frase:
    resultado [c] = resultado.get(c,0) + 1

print (resultado)

'''26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.'''
list_1 = [5, 10, 11, 20, 12, 3]
list_2 = [10, 20, 3, 40, 50, 60]

difference_1 = set(list_1).difference(set(list_2))
difference_2 = set(list_2).difference(set(list_1))

list_difference = list(difference_1.union(difference_2))

print(f"Los elementos que no estan en ambas listas son: {(list_difference)}")

'''27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.'''

def remover_duplicados(cadena):
    no_duplicados = []
    for c in cadena:
        if c not in no_duplicados:
            no_duplicados.append(c)
    return no_duplicados

palabras = ['Aprendiendo', 'lenguaje', 'programacion', 'phyton', 'lenguaje', 'phyton']

print (palabras)
resultado = remover_duplicados(palabras)
print (resultado)

'''28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número'''

print ('Ingrese el numero entero positivo')
i = int(input())
print ('Ingrese el numero menor par')
f = int(input())
suma = 0
print ("**Los numeros pares del rango**")
while i <= f:
    if i % 2 == 0:
        print (i)
    i-=1



'''29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista'''

lista = [5, 4, 7, 2, 1]
 
def promedio_std(lista):
    x = 0
    y = 0
    x = sum(lista) / len(lista)
    total=0.0
    for i in lista:
        total += round((i - x) ** 2,3)
    y = total / (len(lista))
    y= round(y**(1/2),3)
 
    return x,y
 
print(f"El promedio de la lista es: {(promedio_std(lista))}")

'''30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.'''

def encontrar_palabra_mas_larga(palabras):
    palabra_longitud = []

    for p in palabras:
        palabra_longitud.append((len(p), p))
    palabra_longitud.sort()
    return palabra_longitud[-1][1]
palabras = ['practica', 'phyton', 'ejercicio', 'nivel', 'medio']

print(f"La palabra mas larga de la lista es: {(encontrar_palabra_mas_larga(palabras))}")

'''31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos'''

def encontrar_primos(inicial, final):
    primos = []
    for n in range (inicial, final+1):
        contador = 0
        for i in range (1, n+1):
            if n % i == 0:
                contador += 1
        if contador == 2:
            primos.append (n)
    return primos

a = int (input("Escriba un numero entero: "))
b = int(input("Hasta que numero desea que se genere la lista de numeros primos: "))
print(f"Los numeros primos en ese rango son: {(encontrar_primos(a,b))}")

'''32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.'''

texto = 'Ejercicios nivel medio Phyton'
texto_invertido = ''.join(reversed(texto))
print(f"La cadena original es: {(texto)}")
print(f"La cadena invertida es: {(texto_invertido)}")

'''33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.'''

def ordenar_lista_tuplas(tuplas):
    return sorted(tuplas, key=lambda t: t[-1])

listado = [(1, 2), (3, 4), (0, 1), (9, 10)]

resultado = ordenar_lista_tuplas(listado)

print(f"El listado original es: {(listado)}")
print(f"La lista ordenada basada en el ultimo elemento de cada dupla es: {(resultado)}")

'''34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.'''
def obtener_vocales(frase):
    vocales = 'aeiouAEIOU'

    return [c for c in frase if c in vocales]

texto = 'Programando en phyton'
print(f"las vocales contenidas en la frase son: {(obtener_vocales(texto))}")
print(f"El numero de vocales contenidas en la frase es: {(len(obtener_vocales(texto)))}")


'''35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False'''

numero = 11
def es_primo(num):
    contador = 0
    for i in range (1, num+1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False
    
print (es_primo(numero))

