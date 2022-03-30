# ------------------******* FUENTES DE INFORMACIÓN *******-------------------------


# https://scriptverse.academy/tutorials/python-matplotlib-plot-straight-line.html

# http://www.learningaboutelectronics.com/Articles/How-to-plot-multiple-functions-single-graph-in-Python-sympy.php

# https://www.cfm.brown.edu/people/dobrush/am33/SymPy/part1.html

# https://matplotlib.org/stable/api/markers_api.html



import matplotlib.pyplot as plt

import numpy as np

from sympy import *

from sympy.plotting import plot

from sympy import Symbol

import sympy as sym

from sympy.plotting.plot import MatplotlibBackend, Plot



print("\n \n")



# Considere una economía cerrada con precios fijos y desempleo, que se
# comporta de acuerdo con el modelo keynesiano. Se conocen de esta economía los
# siguientes datos:

#  Función de consumo: C = 80 + 0.75*YD
#  Función de recaudación: T = 0.20*Y
#  La inversión es exógena: I0 = 120
#  El gasto del gobierno asciende a G0 = 200.



# Se pide:

# a) Calcule el valor del multiplicador keynesiano, y el valor de equilibrio del ingreso

# b) Calcule los valores de equilibrio de la recaudación de impuestos, el ingreso
#    disponible, el consumo, el ahorro del sector privado y el déficit fiscal.


# create a "symbol" called "Y   "
Y = Symbol('Y')


C_barra = float(80)
c = float(0.75)
s = float(0.25) # lo cual deducimos a partir de c = 0.75
X = float(0)
M = float(0)
G = float(200)
I = float(120)
t = float(0.20)
T = 0.20*Y
A_barra = C_barra + I + G + (X-M)

Mult_Gasto = (1/(1-(c*(1-t))))


# Y = DA = C + I + G + (X-M)

Y_ec = (C_barra + (c*(1-t)*Y)) + I + G + (X - M)


# Cuando vamos a buscar el ingreso de equlibrio, estamos buscando el punto
# en el cual Y = DA

#   (  (1 - (c*(1-t))  ) * Y   = C_barra + I + G + (X - M)

Pend_Y = (c*(1-t))



Y_equ = (C_barra + I + G + (X - M)) / ((1-Pend_Y))


print("Respuesta parte    a): ")

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")


print("La ecuación de la función de ingreso es: ", Y_ec)

print("\n \n")

print("El valor del Multiplicador del Gasto Autónomo es de: ", "{0:.2f}".format(Mult_Gasto))

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")


print("El valor del ingeso de equilibrio es: ", "{0:.2f}".format(Y_equ))

print("\n \n")



# b)

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("Respuesta parte    b): ")


# La recaudación impositiva es: T = 0,20.Y = 0,20 (1000) = 200
T_equ = t*Y_equ

# El ingreso disponible es: YD = Y – T = 1000 – 200 = 800
YD_equ = Y_equ - T_equ

# El consumo es: C = 80 + 0,75.YD = 80 + 0,75 (800) = 680
C_equ = C_barra + c*YD_equ

# El ahorro del sector privado es: S = Y – T – C = YD – C = 800 – 680 = 120
S_equ = Y_equ - T_equ - C_equ

# El déficit fiscal es: G – T = 200 – 200 = 0 por lo tanto hay equilibrio presupuestal.
DF = abs(G - (t*Y_equ))

# Definimos la DA en equilibrio
DA_equ = C_equ + I + G + (X - M)

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("La recaudación impositiva es: ", "{0:.2f}".format(T_equ))

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("El ingreso disponible es de : ", "{0:.2f}".format(YD_equ))

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("El consumo es de : ", "{0:.2f}".format(C_equ))

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("El ahorro privado es de : ", "{0:.2f}".format(S_equ))

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("El Deficit Fiscal es de : ", "{0:.2f}".format(DF))

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")

print("Realizaremos el gráfico de la 'Cruz Keynesiana'   ")

print("\n \n")

print("El valor de la pendiente de la función DA es: ", "{0:.2f}".format(Pend_Y))

print("\n \n")

enter = input("Para continuar, presione    'Enter'    ")

print("\n \n")




def get_sympy_subplots(plot: Plot):
    backend = MatplotlibBackend(plot)

    backend.process_series()
    backend.fig.tight_layout()
    return backend.fig, backend.ax[0]



p = plot(Y_ec, Y, (Y,-2000,2000), title = "Cruz Keynesiana",
legend = True, xlabel = 'Ingreso', ylabel =' Consumo', show = False)


fig, axe = get_sympy_subplots(p)

# add additional plots
axe.plot([Y_equ], [DA_equ], "o")
axe.plot([0], [A_barra], "s")


fig.show()
p.show()


print("--------------****************** FIN DEL CÓDIGO ************------------")

print("\n \n")

enter = input("Para SALIR, presione    'Enter'    ")
