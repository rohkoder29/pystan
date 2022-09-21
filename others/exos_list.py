# exo1
"""
Crear una lista con números positivos desde el teclado en forma ordenada de menor a mayor
hasta ingresar -1. No se debe permitir ingresar elementos desordenados, descartarlos si esto
sucede. Crear la lista mediante una función.

Mostrar la lista por pantalla y luego solicitar el ingreso de un número nuevo por teclado e
insertarlo en la lista de forma que mantenga el ordenamiento indicado. No se permite ordenar
Toda la lista para lograrlo, realizar desplazamientos de los elementos.
"""


# def validar_num() -> int:
#   ''' validar que un numero sea entero y positivo
#       y devolverlo '''
#   while True:
#     try:
#       num = int(input('Ingrese un numero [-1 para salir]: '))
#     except ValueError:
#       print('Por favor, ingrese un numero entero positivo.')
#     else:
#       return num


# def crear_lista() -> list:
#   ''' armar una lista por teclado
#       y devolverla '''
#   lista = []
#   i = 0
#   while True:
#     try:
#       num = validar_num()
#       if num == -1:
#         break
#       assert not lista or num > lista[i-1]
#     except AssertionError:
#       print('El numero debe ser mayor que el anterior.')
#     else:
#       lista.append(num)
#       i += 1
#   return lista


# # MAIN

# # armar la lista por teclado
# nums = crear_lista()
# # mostrar
# print(nums)

# # tomar un numero nuevo
# num_nuevo = validar_num()

# # insertarlo en la lista (do not alterate order)
# start = 0
# end = len(nums)
# while start < end:
#   mid = (start + end) // 2
#   if num_nuevo < nums[mid]:
#       end = mid
#   else:
#       start = mid + 1
# nums.insert(start, num_nuevo)

# # mostrar nueva lista
# print(nums)

#############################

# exo2

# Crear dos listas con números al azar entre 0 y 50 hasta generar el cero de forma que los números
# pares se encuentren en la lista A y los impares en la lista B. Ordenar ambas listas de menor a
# mayor y luego crear una tercera lista intercalando los elementos de forma que mantenga el
# ordenamiento indicado.

# from random import randint


# def crear_listas(lalista1: list, lalista2: list) -> list:
#   ''' crear listas con random entre 0-50 hasta generar 0
#       numeros pares en una lista y numeros impares en la otra '''
#   while True:
#     num = randint(0, 50)
#     if num == 0:
#       break
#     if num % 2 == 0:
#       lalista1.append(num)
#     else:
#       lalista2.append(num)
#   return lalista1, lalista2


# def ordenar_lista(lalista: list) -> list:
#   ''' ordenar una lista de menor a mayor '''
#   for i in range(len(lalista) - 1):
#     for j in range(i + 1, len(lalista)):
#       if lalista[i] > lalista[j]:
#         aux = lalista[i]
#         lalista[i] = lalista[j]
#         lalista[j] = aux
#   return lalista


# def fusionar_listas(lalista1: list, lalista2: list) -> list:
#   ''' fusionar dos listas y ordenar de menor a mayor '''
#   fusion = lalista1 + lalista2
#   ordenar_lista(lalista=fusion)
#   return fusion


# listA, listB = [], []

# lista = crear_listas(lalista1=listA, lalista2=listB)

# print('Elementos lista A')
# print(lista[0], len(lista[0]))
# print(ordenar_lista(lalista=listA))

# print('Elementos lista B')
# print(lista[1], len(lista[1]))
# print(ordenar_lista(lalista=listB))

# print('Todos los elementos')
# todos = fusionar_listas(lalista1=listA, lalista2=listB)
# print(todos, len(todos))

#############################

# exo3 @ /home/rohkuntu/Documents/year2022/py/cli/beg_project/patients_iap.ipynb

#############################

# exo4


# Generar una lista de N elementos de dos dígitos creados al azar. Mostrar la lista.
# Luego Se pide:
# a) Mostrar el promedio y aquellos elementos que sean mayores o iguales al
# promedio, indicando en qué posición se encuentran dentro de la lista.
# b) Ingresar un valor y eliminar todas sus ocurrencias de la lista, no debe quedar
# ningún ejemplar del número a eliminar, informar cuántas veces fue eliminado.
# Desarrollar una función para eliminar todas las ocurrencias de un número y
# retornar la cantidad de veces que fue eliminado.


# from random import randint


# def generar_lista(tope: int) -> list:
#     """ Generar una lista de N elementos de dos dígitos creados al azar. """
#     return [randint(10, 99) for _ in range(tope)]


# def promedio_lista(lalista: list) -> int:
#     """ Calcular el promedio de la lista. """
#     return sum(lalista) // len(lalista)


# def eliminar(lalista: list, valor: int) -> int:
#     """ Eliminar todas las ocurrencias de un número de la lista. """
#     cont = 0
#     for item in lalista:
#         if item == valor:
#             lalista.remove(valor)
#             cont += 1
#     return cont


# N = 20
# elementos = generar_lista(tope=N)
# print(elementos)

# prom = promedio_lista(lalista=elementos)
# print('Promedio de la lista:', prom)

# print('Elementos mayores o igual al promedio:')
# print("Elemento - Posicion") # asumiendo q la posicion empieza en 1
# for i, elem in enumerate(elementos, start=1):
#     temp = print(f'{elem:>8} {i:>10}') if elem >= prom else -1

# numero = int(input('Ingrese valor a eliminar: '))
# if OCURRENCIAS := eliminar(lalista=elementos, valor=numero):
#     print(f'El valor {numero} fue eliminado {OCURRENCIAS}x')
# else:
#     print(f'El valor {numero} no se encuentra en la lista.')

#############################

# exo5

# Crear una lista desde el teclado hasta ingresar -1 sin elementos repetidos y cantidad
# impar de dígitos. Ordenar por Selección según el dígito central de los números
# cargados en la lista.

# def num_lista(num: int) -> int:
#   mid = len(str(num))//2
#   return int(list(str(num))[mid])


# def ordenar_lista(listado: list) -> list:
#   for i in range(len(listado) - 1):
#     for j in range(i + 1, len(listado)):
#       if num_lista(num=listado[i]) > num_lista(num=listado[j]):
#         aux = listado[j]
#         listado[j] = listado[i]
#         listado[i] = aux
#   return listado


# lista = [564, 854, 175, 489, 356, 102, 179, 390, 487]
# num = int(input('Ingrese un numero [-1 para salir]: '))
# while num != -1:
#   if num in lista:
#     print('El numero ya esta en la lista. Ingreasar otro.')
#   elif len(str(num)) % 2 == 1:
#     lista.append(num)
#   else:
#     print('El numero debe tener cantidad impar de digitos.')
#   num = int(input('Ingrese un numero [-1 para salir]: '))

# print(lista)
# ordenada = ordenar_lista(listado=lista)
# print(ordenada)
