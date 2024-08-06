'''1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)


x = 1
while x < 21:
  if x % 2 == 0:
    print (f"los numeros pares son:{x}")
  x+=1

for i in range(100):
   final = 100
   suma = 0
   for i in range (1, final + 1):
    suma = suma + i
print(f"la suma de los numeros del 1 al 100 es igual a",suma)



