# --------------************* FUENTES DE INFORMACIÓN ***********----------------


# https://pynative.com/python-postgresql-tutorial/

# https://pynative.com/python-postgresql-select-data-from-table/

# https://kb.objectrocket.com/postgresql/access-dsn-parameters-for-postgresql-in-python-867

# https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/


# ---------------**************************-------------------------------

# Importamos las Librerias que vamos a utilizar

import psycopg2

from psycopg2 import Error

import matplotlib.pyplot as plt

import numpy as np

# ---------------**************************-------------------------------

# Ahora lo que haremos será conectarnos desde Python a la base de datos
# que creamos con el nombre de "fpp" y traer los datos en ella alojados,
# para luego trabajar con ellos desde Python.

# Crearemos un comando al que se le conoce como "try & except".
# Le estaremos diciendo "try  hacer "tal cosa", y si no funciona (except),
# haz tal otra cosa.

Vacas_A = list()
Autos_A = list()
Vacas_B = list()
Autos_B = list()



try:

    # Nos conectamos a la base de datos a traves de la librería "psycopg2".
    # La base "fpp" se encuentra alojada
    # en el propio equipo, y no en un servidor externo. Por ello debemos
    # señalar que el host es local y no tenemos necesidad de ingresar un
    # puerto.

    conexion_a_base = psycopg2.connect(user="seba",
                                  password="123456",
                                  host="localhost",
                                  # port="5432"
                                  database="fpp")


    # Solicitamos que nos imprima/escriba la información del servidor de SQL

    print("\n", "\n", "\n")

    print("0)   Información del servidor de PostgreSQL", "\n", "\n")

    # You can use a method called "get_dsn_parameters()" that returns a
    # Python dictionary object about the PostgreSQL connection
    # "\n"   es el equivalente al "enter": un salto de linea

    print(conexion_a_base.get_dsn_parameters(), "\n", "\n", "\n", "\n", "\n")



# PASOS:
# 1-  "connect()" = conecta a la base de datos PostgreSQL
# 2- "cursor()"  = crea un objeto utilizando la conexión creada para luego
#              ejecutar solicitudes a la base de datos.
# 3- "execute()" = Ejecuta/corre una solicitud en SQL y devuelve el resultado.
# 4- "fetchall / fetchone / fetchmany" = Lee/muestra el resltado de la solicitud.


# En el paso anterior, tan solo nos conectamos a la base.
# En el paso siguiente, lo que haremos será ejecutar esa conexión
# y poder solicitar distintas órdenes a la base.


    base_fpp = conexion_a_base.cursor()



    # The execute() methods run the SQL query and return the result
    # Solicitamos a la base de datos que nos indique la versión de
    # PostgreSQL y demas
    base_fpp.execute("SELECT version();")


    # cursor.fetchone() method returns a single record or None if
    # no more rows are available.
    # Ahora queremos que nos muestre el resultado de la solicitud ejecutada
    # anteriormente.

    version = base_fpp.fetchone()
    print("1)  Información sobre la Versión de PostgreSQL  ", "\n", "\n",
     version, "\n", "\n", "\n", "\n", "\n")



    # Ahora realizaremos nuestra primera solicitud de información sobre los
    # datos contenidos en la base de datos:  "select * from pais_A"


    base_fpp.execute("select * from pais_A;")

    # Y solicitamos que nos muestre la consulta ejecutada en el paso anterior.
    # Observamos que nos muestra una lista de tuplas con los datos.

    pais_A = base_fpp.fetchall()
    print("2)   Mostrar filas de pais_A  ", "\n",  "\n", pais_A, "\n", "\n", "\n", "\n", "\n")



    # Lo siguiente que quremos hacer es ver los datos de forma un poco mas
    # amigable, por lo que crearemos un loop finito en el que le diremos:
    # "para cada fila de pais_A, mostrame el ID que es lo que esta en la
    # posición cero de la fila cero; el NOMBRE que es lo que está en la
    # posición dos de la fila; etc, junto con el nombre de cada columna"

    print("3)  Mostrar el valor de cada fila y columna del pais_A ",  "\n", "\n")
    for row in pais_A:
        print("Id = ", row[0], )
        print("Nombre = ", row[1])
        print("Produccion_Vacas = ", row[2])
        print("Produccion_Autos  = ", row[3],  "\n", "\n")

    print("\n", "\n")

    for row in pais_A:
        Autos_A.append(row[3])
        Vacas_A.append(row[2])


    print("4)  Mostrar la serie de Autos y Vacas para el Pais A ",  "\n", "\n")

    print("Serie_Autos_Pais_A =", Autos_A)

    print("\n", "\n")

    print("Serie_Vacas_Pais_A =", Vacas_A)

    print("\n", "\n", "\n")



    # Hacemos una segunda consulta, para los dato contenidos en la tabla
    # pais_B


    base_fpp.execute("select * from pais_B")

    pais_B = base_fpp.fetchall()

    print("5)   Mostrar filas de pais_B - ",  "\n",  "\n", pais_B, "\n", "\n", "\n", "\n", "\n")



    print("6)  Mostrar el valor de cada fila y columna del pais_B ",  "\n", "\n")
    for row in pais_B:
        print("Id = ", row[0], )
        print("Nombre = ", row[1])
        print("Produccion_Vacas = ", row[2])
        print("Produccion_Autos  = ", row[3],  "\n", "\n")

    print("\n", "\n")


    for row in pais_B:
        Autos_B.append(row[3])
        Vacas_B.append(row[2])


    print("7)  Mostrar la serie de Autos y Vacas para el Pais B ",  "\n", "\n")

    print("Serie_Autos_Pais_B =", Autos_B)

    print("\n", "\n")

    print("Serie_Vacas_Pais_B =", Vacas_B)


    print("\n", "\n", "\n")




except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)


finally:
    if (conexion_a_base):
        base_fpp.close()
        conexion_a_base.close()
        print("8)  La conexión con PostgreSQL está cerrada",)

print("Terminamos de importar los datos que necesitabamos de la base de datos")

print("\n", "\n", "\n")

a = str("9) Ahora que tenemos las listas de la producción de Autos y Vacas de")

b = str("ambos países, los graficaremos y trabajaremos con ellos")

frase = (a+b)

print(frase)

print("\n", "\n", "\n")


#-----------------******************************--------------------------

#-----------------******************************--------------------------

 #-----------------******************************--------------------------


print("PRIMER EJEMPLO:   función llamada  fpp_1")

# Creamos las coordenadas cartesianas que utilizaremos:  "x" e "y"
#   []  implica que son "Listas"   /  si fueran ()  serian "tuples"

print("\n", "\n", "\n")

def fpp_1():

        x = Autos_A

        y = Vacas_A


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



print("SEGUNDO EJEMPLO:  función llamada  fpp_2")

# Lo que haremos ahora será graficar dos funciones en el mismo gráfico

# Mantenemos las mismas coordenadas el ejemplo anterior, y le indicamos
# que a dicho dibujo la llame  "FPP original"

print("\n", "\n", "\n")

def fpp_2():

    x1 = Autos_A

    y1 = Vacas_A

    plt.plot(x1, y1, label = "FPP_1 original")


    # Creamos las coordenadas del segundo dibujo y le decimos que la llame
    # "FPP: mejora tec. en Vacas", ya que lo que se está representando
    # es un evento exógeno que genera mayor productividad en la producción
    # de vacas.

    x2 = Autos_A

    y2 = [0,36,85,98,101]


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


print("TERCER EJEMPLO:  función llamada  fpp_3")

# Lo que haremos ahora será replicar el primer ejemplo (fpp_1), pero
# ajustando la interfaz del gráfico para que sea mas bonito.


print("\n", "\n", "\n")


def fpp_3():


    x1 = Autos_A

    y1 = Vacas_A


    # Observar que el comando es el mismo que en el primer ejemplo,
    # "plt.plot", solamente que ahora estamos agregando más argumentos
    # al comando (colores de línea, tipo de línea, etc.)
    plt.plot(x1, y1, color='red', linestyle='dashdot', linewidth = 3,
             marker='*', markerfacecolor='yellow', markersize=12)


    # Podemos elegir el rango de cada eje, para visualizar mejor el gráfico
    plt.ylim(-5,85)
    plt.xlim(-5,40)


    plt.xlabel('Autos')

    plt.ylabel('Vacas')

    plt.title('FPP_1 original')

    plt.show()


# fpp_3()




# -----------------******************************--------------------------


print("CUARTO EJEMPLO:  función llamada  fpp_4")


# Lo que haremos ahora será graficar dos funciones en un mismo gráfico


print("\n", "\n", "\n")

def fpp_4():


    # Función 1

    x1 = Autos_A
    y1 = Vacas_A


    # Función 2

    x2 = Autos_A
    y2 = [0,36,85,98,101]


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
