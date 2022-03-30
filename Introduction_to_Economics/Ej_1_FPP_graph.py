# ----------------******* FUENTES DE INFORMACIÓN *******-----------------

# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html

# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

# https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/

# https://www.freecodecamp.org/espanol/news/guia-de-funciones-de-python-con-ejemplos/

# https://www.delftstack.com/es/howto/matplotlib/use-of-pyplot.figure-matplotlib/

# -----------------******************************--------------------------



# Importamos las librerías necesarias para ejecutar el script.

import matplotlib.pyplot as plt

import numpy as np



# -----------------******************************--------------------------

# A todos los ejemplos, los definiremos como "funciones", mediante el
# comando    "def"        def "nombre de funcion"():
# Por convención, el nombre de la función se escribe en minúscula.

# Esto nos es útil a la hora de querer fragmentar el script.

# Lo importante, es lo que está debajo e incluido en la definición
# de la función.


# -----------------******************************--------------------------

#  PRIMER EJEMPLO:   función llamada  fpp_1

# Creamos las coordenadas cartesianas que utilizaremos:  "x" e "y"
#   []  implica que son "Listas"   /  si fueran ()  serian "tuples"

def fpp_1():

        x = [0,32,56,72,80,82]

        y = [34,32,24,16,8,0]


        # Graficamos  "x"  e  "y"

        plt.plot(x, y)


        # Le damos un nombre al eje de las abscisas ("x)" y ordenadas ("y")

        plt.xlabel('Autos')

        plt.ylabel('Vacas')


        # Le damos un noombre al gráfico

        plt.title('FPP_1')


        # Le damos la orden al programa que nos muestre el gráfico creado, con sus
        # respectivos ejes y título.

        plt.show()

# fpp_1()



# -----------------******************************--------------------------



#  SEGUNDO EJEMPLO:  función llamada  fpp_2

# Lo que haremos ahora será graficar dos funciones en el mismo gráfico

# Mantenemos las mismas coordenadas el ejemplo anterior, y le indicamos
# que a dicho dibujo la llame  "FPP original"

def fpp_2():

    x1 = [0,32,56,72,80,82]

    y1 = [34,32,24,16,8,0]

    plt.plot(x1, y1, label = "FPP_1 original")


    # Creamos las coordenadas del segundo dibujo y le decimos que la llame
    # "FPP: mejora tec. en Vacas", ya que lo que se está representando
    # es un evento exógeno que genera mayor productividad en la producción
    # de vacas.

    x2 = [0,32,56,72,80,82]

    y2 = [40,36,27,19,9,0]

    plt.plot(x2, y2, label = "FPP: mejora tec. en Vacas")


    # Le damos un nombre al eje de las abscisas ("x)" y ordenadas ("y")

    plt.xlabel('Autos')

    plt.ylabel('Vacas')


    # Le damos un noombre al gráfico

    plt.title('FPP_2: mejora tecnológica SOLO en Vacas')


    # Mostramos el nombre de cada uno de los gráficos dibujados

    plt.legend()


    # Le damos la orden al programa que nos muestre el gráfico creado, con sus
    # respectivos ejes y título.

    plt.show()


# fpp_2()



# -----------------******************************--------------------------


#  TERCER EJEMPLO:  función llamada  fpp_3

# Lo que haremos ahora será replicar el primer ejemplo (fpp_1), pero
# ajustando la interfaz del gráfico para que sea mas bonito.



def fpp_3():


    x1 = [0,32,56,72,80,82]

    y1 = [34,32,24,16,8,0]


    # Observar que el comando es el mismo que en el primer ejemplo,
    # "plt.plot", solamente que ahora estamos agregando más argumentos
    # al comando (colores de línea, tipo de línea, etc.)
    plt.plot(x1, y1, color='red', linestyle='dashdot', linewidth = 3,
             marker='*', markerfacecolor='yellow', markersize=12)


    # Podemos elegir el rango de cada eje, para visualizar mejor el gráfico
    plt.ylim(-5,45)
    plt.xlim(-5,95)


    plt.xlabel('Autos')

    plt.ylabel('Vacas')

    plt.title('FPP_1 original')

    plt.show()


# fpp_3()




# -----------------******************************--------------------------


#  CUARTO EJEMPLO:  función llamada  fpp_4


# Lo que haremos ahora será graficar dos funciones en un mismo gráfico

def fpp_4():


    # Función 1

    x1 = [0,32,56,72,80,82]
    y1 = [34,32,24,16,8,0]


    # Función 2

    x2 = [0,32,56,72,80,82]
    y2 = [40,36,27,19,9,0]


    # Utilizaremos el comando   plt.figure()   para crear un objeto-figura,
    # en la cual luego insertar los dos graficos

    plt.figure()


    # Creamos la primera de las dos imágenes que graficaremos y visualizaremos
    # en la figura creada.
    # Atención que la numeración de los "subplot" tiene que tener tres dígitos
    # no pudiendo ser 0 (cero) ninguno de ellos.

    plt.subplot(211)

    # Graficamos  x1, y1

    plt.plot(x1, y1, color='red', linestyle='dashdot', linewidth = 3,
             marker='*', markerfacecolor='yellow', markersize=12, label = "FPP_1 original")


    plt.xlabel('Autos')

    plt.ylabel('Vacas')

    plt.title('FPP_1 original')


    # Creamos la segunda imagen que graficaremos, graficando (x1, y1) y (x2, y2)
    # en la misma sub-imagen

    plt.subplot(212)

    plt.plot(x1, y1, color='red', linestyle='dashdot', linewidth = 3,
             marker='*', markerfacecolor='yellow', markersize=12,label = "FPP_1 original")

    plt.plot(x2, y2, color='blue', linestyle='solid', linewidth = 3,
             marker='*', markerfacecolor='green', markersize=12,label = "FPP: mejora tec. en Vacas")

    plt.xlabel('Autos')

    plt.ylabel('Vacas')

    plt.title('FPP_2: mejora tecnológica SOLO en Vacas')

    plt.show()


# fpp_4()








# -----------------******************************--------------------------


#  QUINTO EJEMPLO:  función llamada  fpp_5


# Lo que haremos ahora será observar puntos interiores, exteriores y por
# sobre la FPP


def fpp_5():

    x1 = [0,32,56,72,80,82]

    y1 = [34,32,24,16,8,0]

    plt.plot(x1, y1, label = "FPP_1 original")

    # Creamos las coordenadas del segundo dibujo y le decimos que la llame
    # "FPP: mejora tec. en Vacas", ya que lo que se está representando
    # es un evento exógeno que genera mayor productividad en la producción
    # de vacas.

    x2 = [36]

    y2 = [22]

    plt.plot(x2, y2, label = "Punto Interior a la FPP", marker='*')




    x3 = [60]

    y3 = [36]

    plt.plot(x3, y3, label = "Punto Exterior a la FPP", marker='*')




    x4 = [32]

    y4 = [32]

    plt.plot(x4, y4, label = "Punto sobre la FPP", marker='d')


    # Le damos un nombre al eje de las abscisas ("x)" y ordenadas ("y")

    plt.xlabel('Autos')

    plt.ylabel('Vacas')


    # Le damos un noombre al gráfico

    plt.title('Comparando puntos de la FPP')


    # Mostramos el nombre de cada uno de los gráficos dibujados

    plt.legend()


    # Le damos la orden al programa que nos muestre el gráfico creado, con sus
    # respectivos ejes y título.

    plt.show()


# fpp_5()





# -----------------******************************--------------------------

# Este comando,   if __name__ == '__main__':      lo que hace es
#  "cambiar el punto de arranque de lectura del código".
# Ya no arranca en la línea 1, sino que ejecuta TODO lo que esté por debajo
# de   if __name__ == '__main__':
# Es decir, que yo puedo crear todas las funciones al comienzo del código
# y luego llamarlas debajo de  if __name__ == '__main__':
# De esa manera, indirectamente, estoy fraccionando el script para
# poder ejecutarlo de a partes.

if __name__ == '__main__':

    fpp_1()

    fpp_2()

    fpp_3()

    fpp_4()

    fpp_5()
