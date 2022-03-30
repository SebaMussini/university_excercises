#  ----------------------**********FUENTES DE INFORMACIÓN ************--------------


# https://stackoverflow.com/questions/66136166/scraping-and-downloading-excel-files-using-python-from-url

# https://stackoverflow.com/questions/62597887/python-request-get-response-object-to-download-xlsx-file-from-url-saves-excel-fi

# https://stackoverflow.com/questions/20986640/scraping-download-files-from-url

# https://stackoverflow.com/questions/25415405/downloading-an-excel-file-from-the-web-in-python

# https://www.w3schools.com/tags/tag_a.asp

# https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3



# Importamos las librerías que vamos a necesitar

from bs4 import BeautifulSoup as bs
import requests


# Especificamos la url a la cual realizaremos el scraping

URL = 'https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Series-Estadisticas-del-PIB-por-industrias.aspx'


# Definimos una función llamada "get_soup" la cual realizará el procedimiento
#  "request.get" de la librería BeautifulSoup (bs) al argumento que indiquemos,
# siendo en este caso, la URL anteriormente definida.

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')


# Creamos una lista vacía, la cual utilizaremos más adelante.

archivos = list()


# Ahora comenzamos el scraping propiamente dicho.

# Lo primero que hacemos es que busque en la URL especificada, todas las
# líneas que tengan como tag "a" (anchor tag) y que luego nos traiga
# los "href" asociados a dichos "a".
# Van a ser varios, pero nosotros no queremos todos esos href, sino algunos
# en particular: los que contengan las palabras "Cuentas Nacionales"
# Debemos agregar una condición de que los links sean DISTINTOS (!=) a
#  "None", pues si no lo hacemos el scraping se corta.
# Por último, le indicamos que nos agregue los links que encontró en la
# lista llamada "archivos" que creamos al principio.

for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    #print(file_link)
    if file_link != None:
        if "Cuentas Nacionales" in file_link:
            #print(file_link)
            archivos.append(file_link)

# Vemos la lista "archivos" conteniendo los links que nos interesaba
# screapear. Todos ellos accden a un archivo.xlsx diferente, que bajaremos
# de la web.

print(archivos)


# Para cada uno de los elementos de la lista, le indicamos que los baje
# de la web y los guarde como un archivo.xlsx de excel, con los nombres
# correspondientes.

resp = requests.get(archivos[0])
output = open('Actividades_K.xlsx', 'wb')
output.write(resp.content)
output.close()


resp = requests.get(archivos[1])
output = open('Actividades_C.xlsx', 'wb')
output.write(resp.content)
output.close()


resp = requests.get(archivos[2])
output = open('Actividades_IVF.xlsx', 'wb')
output.write(resp.content)
output.close()


resp = requests.get(archivos[3])
output = open('IPI.xlsx', 'wb')
output.write(resp.content)
output.close()


resp = requests.get(archivos[3])
output = open('Desestacionalizado.xlsx', 'wb')
output.write(resp.content)
output.close()


print("-------------**************FIN DEL CÓDIGO***********-----------")

salir = input("Para SALIR, presione   'Enter'  ")
