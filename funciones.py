'''1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Define una función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
'''

def suma_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
lista = [10, 5]
print(suma_lista(lista))



def factorial(num):
    if num < 0:
        print("Factorial de un numero negativo no existe")

    elif num == 0:
        return 1

    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact
num = 2
print("El factorial de", num, "es", factorial(num))


def primo(num):
 if num < 2: #si es menor de 2 no es primo, devolverá Falso
   return "No es un numero primo"
 for i in range(2, num): #un ciclo desde el 2 hasta el num de entrada
   if num % i == 0: #si el resto da 0 no es primo, devuelve Falso
    return "No es un numero primo"
 return "Si es un numero primo"

print(primo(7))

def suma_lista(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma
mi_lista = [5, 10, 3, 1, 2]
print(suma_lista(mi_lista))

cadena = "Prueba Phyton"
cadena_invertida = cadena[::-1]
print(cadena_invertida)
