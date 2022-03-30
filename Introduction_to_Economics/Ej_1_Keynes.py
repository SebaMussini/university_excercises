# ------------------******* FUENTES DE INFORMACIÓN *******-------------------------


# https://scriptverse.academy/tutorials/python-matplotlib-plot-straight-line.html

# http://www.learningaboutelectronics.com/Articles/How-to-plot-multiple-functions-single-graph-in-Python-sympy.php

# https://www.cfm.brown.edu/people/dobrush/am33/SymPy/part1.html



import matplotlib.pyplot as plt

import numpy as np

from sympy import *

from sympy.plotting import plot

from sympy import Symbol

import sympy as sym



print("\n \n")


# Asuma una economía SIN Gobierno y SIN comercio exterior (no hay
# exportaciones ni importaciones), en la cual el ingreso que no se consume,
# se ahorra.

# Se sabe que el Consumo asciende a 200, independientemente del nivel de
# ingresos ("C barra"). A su vez, por cada unidad
# extra de ingreso, se ahorra 1/4 parte de esa unidad adicional.


# Se pide:

# a) Escriba una ecuación que refleje que puede hacerse con el ingreso.
# b) Escriba una ecuación que refleje la Función de Ahorro
# c) Escriba una ecuación que refleje la Función de Consumo
# d) Indique el valor de la pendiente de la Función de Consumo.
# e) Grafique la Función de Consumo y la Función de Ahorro en un mismo eje.

C_barra = 200
s = 0.25 # lo cual implica que c = 0.75, pues todo lo que no se ahorra, se consume
c = 0.75
X = 0
M = 0
G = 0

# create a "symbol" called x
Y = Symbol('Y')

# a) Y = C + S

print("Respuesta parte    a): ")


print("\n \n")

print("Con el ingreso pueden hacerse dos cosas: Consumir (C) y Ahorrar (S).")
print("Todo el ingreso debe agotarse entre ambas opciones")

print("\n \n")

# b)

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("Respuesta parte    b): ")


print("\n \n")

# S = Y - C
# S = Y - (C_barra + (c*Y))
S = -C_barra + ((1-c)*Y)

print("La ecuación de la función de ahorro (S) es: S = ", S)

print("\n \n")

# c)

C = Y - S

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("Respuesta parte    c): ")

print("\n \n")

print("La ecuación de la función de consumo (C) es: C = ", C)

print("\n \n")


print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")


# d)

print("Respuesta parte    d): ")

print("\n \n")

print("El valor de la pendiente de la función de consumo es: ", c)

print("\n \n")

print("El valor de la pendiente de la función de ahorro es: ", s)

print("\n \n")


# e)


enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("Respuesta parte    e): ")

print("\n \n")


graph= plot(C, S, (Y,-1000,1000), title = "Función de Consumo",
legend = True, xlabel = 'Ingreso', ylabel =' Consumo', show = False)

graph.show()



while True:
    try:
        consulta = str(input("¿Desea guardar el gráfico generado?: "))
        if consulta == "Si":
            print("\n \n")
            graph.save('Grafico_Keynes.png')
            print("El gráfico se ha guardado con el nombre 'Grafico_Keynes.png'")
            print("\n \n")
            break
        elif consulta == "No":
            print("\n \n")
            print("Saliendo del programa........")
            print("\n \n")
            break
        else:
            print("\n \n")
            print("Debe responder   'Si'   o     'No'")
            print("\n \n")
            continue
    except:
        print("Debe responder   'Si'   o     'No'")


print("\n \n")


print("--------------****************** FIN DEL CÓDIGO ************------------")

print("\n \n")

enter = input("Para SALIR, presione    'Enter'    ")
