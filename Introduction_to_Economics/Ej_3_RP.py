

import matplotlib.pyplot as plt

import numpy as np



print("\n \n")

while True:
    try:
        Ingreso = float(input("Ingrese el monto de dinero disponible: "))
        if not 7000 <= Ingreso <= 20000:
            print("Error: el valor de Ingreso debe estar entre 7000 y 20000")
            print("\n \n")
        else:
            break
    except:
        print("El ingreso debe ser un número no negativo")


print("\n \n")


print("El monto de dinero disponible es de: ", Ingreso)

print("\n \n")


while True:
    try:
        Propa = float(input("Ingrese el Precio de la ropa: "))
        if not 70 <= Propa <= 200:
            print("Error: el Precio de la ropa debe estar entre 70 y 200")
            print("\n \n")
        else:
            break
    except:
        print("El precio debe ser un número no negativo")


print("\n \n")

print("El precio de la ropa es de: ", Propa)

print("\n \n")



while True:
    try:
        Pinternet = float(input("Ingrese el Precio de Internet: "))
        if not 0.5 <= Pinternet <= 12:
            print("Error: el Precio de Internet debe estar entre 0.5 y 12")
            print("\n \n")
        else:
            break
    except:
        print("El precio debe ser un número no negativo")


print("\n \n")

print("El precio de internet es de: ", Pinternet)

print("\n \n")


continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

EcuRP = "RP =   (Propa*Qropa)  +  (Pinternet*Qinternet)  -  (Ingreso)  "

print("La Ecuación de la Restricción Presupuestaria es: ", EcuRP)

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

MaxRopa = (Ingreso/Propa)

MaxInternet = (Ingreso/Pinternet)

print("Si gastara TODO mi ingreso solamente en ropa, ¿qué cantidad podría comprar?")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print(MaxRopa, "unidades de ropa")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")


print("Si gastara TODO mi ingreso solamente en Internet, ¿qué cantidad podría comprar?")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print(MaxInternet, "unidades de internet")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")


print("Grafiquemos entonces nuestra Restricción Presupuestal: ")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

def RP_1():

        ropa = [0, MaxRopa]

        internet = [MaxInternet, 0]


        plt.plot(ropa, internet, color='blue', linestyle='solid', linewidth = 2,
                 marker='', markerfacecolor='red', markersize=8)


        # Podemos elegir el rango de cada eje, para visualizar mejor el gráfico
        plt.xlim(0, MaxRopa*1.02)
        plt.ylim(0, MaxInternet*1.02)



        # Le damos un nombre al eje de las abscisas ("x)" y ordenadas ("y")

        plt.xlabel('Ropa')

        plt.ylabel('Internet')


        # Le damos un noombre al gráfico

        plt.title('Restricción Presupuestaria')


        # Le damos la orden al programa que nos muestre el gráfico creado, con sus
        # respectivos ejes y título.

        plt.show()

RP_1()

print("\n \n")


continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print("¿Cuál es el valor de la pendiente del gráfico?")

print("\n \n")

pendiente1 = -(Propa/Pinternet)

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print("El valor de la pendiente es: ", pendiente1)

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")


print("Si decidieramos consumir el ???? % de nuestro presupuesto en unidades de Internet, ¿cuánta internet compraríamos?")

print("\n \n")



while True:
    try:
        DinerodestinadoaInternet = float(input("¿Qué proporción del ingreso desea destinar a comprar internet?: "))
        if not 0 <= DinerodestinadoaInternet <= 1:
            print("Error: la proporción debe estar entre 0 y 1")
            print("\n \n")
        else:
            break
    except:
        print("La porporción debe ser un número entre 0 y 1")


print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

Qinternet = (Ingreso/Pinternet)*DinerodestinadoaInternet

print("Podriamos comprar ", Qinternet, " unidades de internet")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

EcuRP = "(Propa*Qropa)  +  (Pinternet*Qinternet)  -  (Ingreso)"


print("¿Y cuantas unidades de Ropa podríamos comprar con el dinero restante?")

Qropa = (Ingreso - (Pinternet*Qinternet) )  / (Propa)

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print("Podriamos comprar ", Qropa, " unidades de ropa")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print("Grafiquemos este punto particular de la RP en el cual Qropa =", Qropa, "y Qinternet =", Qinternet)

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

def RP_2():

        ropa = [0, MaxRopa]

        internet = [MaxInternet, 0]


        plt.plot(ropa, internet, color='blue', linestyle='solid', linewidth = 2,
                 marker='', markerfacecolor='red', markersize=8)


        ropa0 = [Qropa]

        internet0 = [Qinternet]


        plt.plot(ropa0, internet0, color='green', linestyle='solid', linewidth = 8,
                 marker='*', markerfacecolor='yellow', markersize=18)


        # Podemos elegir el rango de cada eje, para visualizar mejor el gráfico
        plt.xlim(0, MaxRopa*1.02)
        plt.ylim(0, MaxInternet*1.02)



        # Le damos un nombre al eje de las abscisas ("x)" y ordenadas ("y")

        plt.xlabel('Ropa')

        plt.ylabel('Internet')


        # Le damos un noombre al gráfico

        plt.title('Restricción Presupuestaria')


        # Le damos la orden al programa que nos muestre el gráfico creado, con sus
        # respectivos ejes y título.

        plt.show()

RP_2()



print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")


# Suponga que ahora su familia le dice que se hace cargo del 25%
# de su gasto en ropa. Estime la nueva ecuación de la RP y grafique ambas
# en un mismo gráfico.

EcuRP_2 = "RP =   (Propa*(1-0.25)*Qropa)  +  (Pinternet*Qinternet)  -  (Ingreso)  "


print("La Ecuación de la Restricción Presupuestaria es: ", EcuRP_2)

MaxRopa_2 = (Ingreso/((1-0.25)*Propa))

MaxInternet_2 = (Ingreso/Pinternet)

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")


print("Grafiquemos ambas RP: ")

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")


def RP_3():

        ropa = [0, MaxRopa]

        internet = [MaxInternet, 0]


        plt.plot(ropa, internet, color='blue', linestyle='solid', linewidth = 2,
                 marker='', markerfacecolor='red', markersize=8)


        ropa2 = [0, MaxRopa_2]

        internet2 = [MaxInternet_2, 0]


        plt.plot(ropa2, internet2, color='yellow', linestyle='solid', linewidth = 2,
                 marker='', markerfacecolor='green', markersize=8)


        # Podemos elegir el rango de cada eje, para visualizar mejor el gráfico
        plt.xlim(0, MaxRopa_2*1.02)
        plt.ylim(0, MaxInternet_2*1.02)



        # Le damos un nombre al eje de las abscisas ("x)" y ordenadas ("y")

        plt.xlabel('Ropa')

        plt.ylabel('Internet')


        # Le damos un noombre al gráfico

        plt.title('Restricción Presupuestaria')


        # Le damos la orden al programa que nos muestre el gráfico creado, con sus
        # respectivos ejes y título.

        plt.show()

RP_3()

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print("¿Cuál es el valor de la pendiente del gráfico?")

pendiente2 = -(((1-0.25)*Propa)/(Pinternet))

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")

print("El valor de la pendiente es: ", pendiente2)

print("\n \n")

continuar = input("Para continuar, presione    'Enter'       ")

print("\n \n")


print("--------*****************  FIN DEL SCRIPT  ***********---------------")
