# -*- coding: utf-8 -*-
'''
Ejercicio No 1
Autor : alexandra cordoba
Cliente : SENASoft 
Fecha: 12/08/2022
Version: 1

'''

#----------------------
#	Constantes
#----------------------
#----------------------
# Variables globales
#----------------------
histograma = []
calificacion_valida = ['a','b','c','d','e']
#----------------------
# Procedimientos
#----------------------
# procedimiento para agregar los datos ingresados que son validos al histograma
def elementos_colecion(num_elementos,histograma):
    for i in range(num_elementos):
        nota = validar_elementos(calificacion_valida) # Cada valor ingresado debe ser una letra (a b c d y e). Validar que no sean otras letras.
        histograma.append(nota)
# procedimiento para  Calcular el histograma
def calcular_elementos(vector):
    a = 0
    b = 0
    c = 0
    d = 0 
    e = 0

    for j in vector:
        if j == 'a':
            a += 1
        elif j == 'b':
            b += 1
        elif j == 'c':
            c += 1         
        elif j == 'd':
                d += 1    
        elif j == 'e':
            e += 1
    print('histograma numerico')
    mostrar_numerico(a,b,c,d,e)
    print('histograma asteristico')
    mostrar_asteristico(a,b,c,d,e)


#procedimiento para  mostrar el histograma numerico
def mostrar_numerico(a,b,c,d,e): 
    if a > 0 :
        print('a:'+ str(a))
    if b > 0:
        print('b:'+ str(b))
    if c > 0:
        print('c:'+ str(c))
    if d > 0:
        print('d:'+ str(d)) 
    if e > 0:
        print('e:'+ str(e)) 

#procedimiento para mostrar el histograma asteristico
def mostrar_asteristico(a,b,c,d,e): 
    asteristicoA = ''
    asteristicoB = ''
    asteristicoC = ''
    asteristicoD = ''
    asteristicoE = ''
    if a > 0 :
        for i in range(a):
            asteristicoA = asteristico(a)
        print('a:'+ asteristicoA) 
    if b > 0:
        asteristicoB = asteristico(b)
        print('b:'+ asteristicoB) 
    if c > 0:
        asteristicoC = asteristico(c)
        print('c:'+ asteristicoC) 
    if d > 0:
        asteristicoD = asteristico(d)
        print('d:'+ asteristicoD) 
    if e > 0:
        asteristicoE = asteristico(e)
        print('e:'+ asteristicoE)
    

#----------------------
# Clases 
#----------------------

#----------------------
# Funciones
#----------------------

#validar el numero de personas entrenvistadas no puede ser mayor a 100
def num_elementos():
    while True:
        num_personas = int (input('ingrese el numero de elemetos de la coleccion'))
        if num_personas > 0  and num_personas <= 100: #valida que numero de entrevistados sea mayor a 0 y menor que 100
            return num_personas
        else:
            print('ingrese un numero entre 1 y 100')
            continue
# primera funcion para definir si la letra ingresada es valida
def validar_elementos(calificacion_valida):
    while True:
        calificacionin = input('ingrese la calificacion')
        for i in calificacion_valida:
            if calificacionin == i: # valida que la calificacion ingresada sea valida
                return calificacionin
                break         
            else:
                continue
# agrega los asteristicos 
def asteristico(num):
    a = ''
    for i in range(num):
        a += '*'
    return a
#----------------------
# Programa Principal
#----------------------
def main():
    num_personas = num_elementos()
    elementos_colecion(num_personas,histograma)
    print('histograma', histograma)
    calcular_elementos(histograma)

if __name__ == '__main__':
    main()