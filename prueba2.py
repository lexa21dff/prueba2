# -*- coding: utf-8 -*-
'''
Ejercicio No 2
Autor : alexandra cordoba
Cliente :
Fecha: 12/08/2022
Version: 1

'''
import random

# ---------------- 
# Constantes
# ----------------

# ----------------
# Variables globales
# ----------------
# matriz minimo 2x2 y maximo 10x 10
A = []
B = []
C = []
At = []
Bt = []
Cm =[]
trazarA = 0
trazarB = 0

# ----------------
# Procedimientos
# ----------------

# Procedimiento para agregar datos a una matriz
def ingresar (tamaño,matriz):
    for i in range(tamaño):
        matriz.append([])
        for j in range(tamaño):
            numero = random.randint(0, 20)
            matriz[i].append(numero)

#procedimiento para sumar dos matrices
def suma_matrices(tamaño,matriz1,matriz2,matriz3):
    for i in range(tamaño):
        matriz3.append([])
        for j in range(tamaño):
            suma = matriz1[i][j] + matriz2[i][j]
            matriz3[i].append(suma)
            suma = 0

#procedimiento para una matriz tranpuesta
def matriz_transpuesta(tamaño,A,At):
    for i in range(tamaño):
        At.append([])
        for j in range(tamaño):
            temporal = A[j][i]
            At[i].append(temporal)

# funcion para multiplicar matrices
def multiplicacion_matricez(tamaño,A,B,Cm):
    for i in range(tamaño):
        Cm.append([])
        for j in range(tamaño):
            suma = 0
            for p in range(tamaño):
                multiplicacion = A[i][p] * B[p][j]
                suma = suma + multiplicacion
            Cm[i].append(suma)

# funcion para mostrar una matriz

def mostrar_matriz(matriz,tamaño):
    for i in range(tamaño):
        for j in range(tamaño):
            print(matriz[i][j], end='\t')
            if j == tamaño-1:
                print("\n")
            
# ----------------
# Clases 
# ----------------

# ----------------
# Funciones
# funcion para validar el tamaño de la matriz 
def tamaño_de_la_matriz ():
    while True:
        tamaño = int (input('ingrese el tamaño de la matriz '))
        if tamaño >= 2 and tamaño<=10: # valida el támaño de la matriz
            return tamaño
        else:
            continue
#funcion para trazar una matriz 
def trazar_una_matriz(tamaño,matriz):
    suma = 0
    for i in range(tamaño):
        temporal = matriz[i][i]
        suma = suma + temporal
    return suma
# ----------------

# ----------------
# Programa Principal
# ----------------
def main ():
    tamaño = tamaño_de_la_matriz()

    print('matriz A')
    ingresar(tamaño,A)
    mostrar_matriz(A,tamaño)

    print('matriz B')
    ingresar(tamaño,B)
    mostrar_matriz(B,tamaño)

    print('suma de las matrices A y B')
    suma_matrices(tamaño,A,B,C)
    mostrar_matriz(C,tamaño)

    print('la matriz A traspuesta')
    matriz_transpuesta(tamaño,A,At)
    mostrar_matriz(At,tamaño)

    print('la matriz B traspuesta')
    matriz_transpuesta(tamaño,B,Bt)
    mostrar_matriz(Bt,tamaño)

    trazarA = trazar_una_matriz(tamaño,A)
    print('traza de la matriz A '+ str(trazarA))

    trazarB = trazar_una_matriz(tamaño,B)
    print('traza de la matriz b ' + str(trazarB) )

    print('multiplicacion de la matriz A y B')
    multiplicacion_matricez(tamaño,A,B,Cm)
    mostrar_matriz(Cm,tamaño)

if __name__ == '__main__':
        main()