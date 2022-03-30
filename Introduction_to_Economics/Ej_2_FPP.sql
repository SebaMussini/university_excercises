---------******************  FUENTES DE INFORMACIÓN **********-----------------

--  https://alvinalexander.com/blog/post/postgresql/log-in-postgresql-database/

--  https://alvinalexander.com/blog/post/postgresql/what-are-available-listing-commands-in-postgresql/

--  https://www.pluralsight.com/guides/importing-data-from-a-database-using-python

--  https://www.w3schools.com/sql/sql_unique.asp

--  https://stackoverflow.com/questions/37984733/postgresql-database-export-to-sql-file/37985097


-- ****** IMPORTANTE:  instalar      pip install psycopg2-binary



--------------------******************************------------------------


-- Para trabajar con bases de datos relacionales a través del lenguaje SQL,
-- utilizaremos el programa     "Postgresql"



--------------------******************************------------------------


-- Lo primero que haremos, será crear un usuario dueño de una base de datos
-- a ser creada luego.
-- Para crear Usuario (NO super-usuario) asociado a una base de datos,
-- debemos ingresar el siguiente comando en la terminal de Ubuntu:

sudo -u postgres psql



-- El usuario se llamará  "seba" y su contraseña será "123456"

CREATE USER seba WITH PASSWORD '123456';

-- El usuario "seba" será el dueño de una base de datos que se llamará  "fpp"

CREATE DATABASE fpp WITH OWNER 'seba';


-- Luego de creado el usuario y su base de datos, debemos ingresar a ella, y
-- lo hacemos de la siguiente manera:

-- If you are logged into the same computer that Postgres is running on you
-- can use the following psql login command, specifying the
-- database (mydb) and username (myuser):

-- psql -d mydb -U myuser

-- En nuestro caso  "d" es "fpp"  y   "-U" es  "seba"

psql -d fpp -U seba


-- If you need to log into a Postgres database on a server
-- named myhost, you can use this Postgres login command:

-- psql -h myhost -d mydb -U myuser


--------------------******************************------------------------


-- Lo primero que haremos, será correr las siguientes tres sentencias para
-- eliminar esas tres tablas, en caso que ya existieran.


DROP TABLE pais_A;
DROP TABLE pais_B;
DROP TABLE mundo;


-- Ahora crearemos nuestra primera base de datos, a la que llamaremos
-- "pais_A", y que contará con las siguientes columnas: "id", "Nombre",
-- "Produccion_Vacas" y "Produccion_Autos"

-- A su vez, cada una de esas columnas tienen una descripción sobre si misma.

-- Por ejemplo, tanto "Produccion_Vacas" como "Produccion_Autos", comparten
-- su descripción:  contendrán números (REAL) y serán valores únicos que no
-- podrán repetirse (UNIQUE)
-- The UNIQUE constraint ensures that all values in a column are different.

-- "Nombre", será un campo donde habrá Texto (TEXT)

-- "id"  es un identificador que utilizaremos en la tabla, el cual tiene
-- como atributo ser "SERIAL", lo que significa que ese campo se
-- auto-completará automáticamente y de forma incremental a medida que se
-- agreguen registros/filas a la tabla.
-- SERIAL data type allows you to automatically generate unique integer
-- numbers (IDs, identity, auto-increment, sequence) for a column.

-- Por último, indicaremos que "id"  será la Clave Primaria (PRIMARY KEY) de
-- la tabla. Ello significa que cada registro de la tabla se identificará
-- con la clave primaria, en nuestro caso, "id".
-- The PRIMARY KEY constraint uniquely identifies each record in a table.
-- Primary keys must contain UNIQUE values, and cannot contain NULL values.
-- A table can have only ONE primary key


-- Creamos la tabla "pais_A"

CREATE TABLE pais_A (
  id SERIAL,
  Nombre TEXT,
  Produccion_Vacas REAL UNIQUE,
  Produccion_Autos REAL UNIQUE,
  PRIMARY KEY (id)
);


-- Creamos la tabla "pais_B"

CREATE TABLE pais_B (
  id SERIAL,
  Nombre TEXT,
  Produccion_Vacas REAL UNIQUE,
  Produccion_Autos REAL UNIQUE,
  PRIMARY KEY (id)
);


-- Vemos el contenido de cada una de esas tablas, las cuales estan vacias
-- pero sí están creadas las columnas que corresponden.

SELECT * FROM pais_A;
SELECT * FROM pais_B;



-- CREATE TABLE mundo (
--  id SERIAL,
--  Nombre TEXT,
--  pais_A_id INTEGER REFERENCES pais_A(id) ON DELETE CASCADE,
--  pais_B_id INTEGER REFERENCES pais_A(id) ON DELETE CASCADE,
--  PRIMARY KEY (id)
--);




-- Cargamos datos en la tabla "pais_A"

INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '0', '34');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '32', '32');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '72', '16');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '80', '8');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '82', '0');


-- Vemos ahora que la tabla "pais_A" ya tiene datos y que no hubo problemas
-- u errors en su carga.

SELECT * FROM pais_A;



-- Pasamos ahora a cargar datos en la tabla "pais_B", pero ATENCIÓN!!!, pues
-- en este caso, surgirá un error, pues estaremos violando la condición
-- de  UNIQUE  que impusimos para las columnas "Produccion_Vacas" y
-- "Produccion_Autos".  Sucede en la línea número  174   se genera un dato
-- repetido para la columna "Produccion_Autos":   el valor  34
-- Al otorgar la restricción de UNIQUE, no estamos permitiendo valores repetidos


INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '0', '68');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '55', '64');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '92', '52');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '116', '34');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '121', '34');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '-850', '-32');

-- Tenemos varias opciones para resolver este problema. Elegiremos quitar
-- la condición de UNIQUE de "Produccion_Vacas" y "Produccion_Autos"


-- Eliminamos las tablas que hemos creado y con ellas, los registros

DROP TABLE pais_A;
DROP TABLE pais_B;
DROP TABLE mundo;


CREATE TABLE pais_A (
  id SERIAL,
  Nombre TEXT,
  Produccion_Vacas REAL,
  Produccion_Autos REAL,
  PRIMARY KEY (id)
);




CREATE TABLE pais_B (
  id SERIAL,
  Nombre TEXT,
  Produccion_Vacas REAL,
  Produccion_Autos REAL,
  PRIMARY KEY (id)
);




-- CREATE TABLE mundo (
--  id SERIAL,
--  Nombre TEXT,
--  pais_A_id INTEGER REFERENCES pais_A(id) ON DELETE CASCADE,
--  pais_B_id INTEGER REFERENCES pais_A(id) ON DELETE CASCADE,
--  PRIMARY KEY (id)
--);




INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '0', '34');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '32', '32');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '72', '16');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '80', '8');
INSERT INTO pais_A (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais A', '82', '0');


-- Observar que ahora no tengo problemas al ingresar el dato de la línea 235
-- del script, que registra dos veces el valor  34  para "Produccion_Autos"

INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '0', '68');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '55', '64');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '92', '52');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '116', '34');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '121', '34');
INSERT INTO pais_B (Nombre, Produccion_Vacas, Produccion_Autos) VALUES ('Pais B', '-850', '-32');



--------************** Comandos importantes:   *********-------------

-- 1) Table, index, view, or sequence
-- \d

-- 2) Tables
-- \dt

-- 3) Databases
-- \l

-- 4) Para salir de Postgresql
-- \q



----------------------*************************-----------------------


-- Vemos los valores cargados en nuestras dos tablas, siendo  5 en "pais_A"
-- y 6 en "pais_B"

SELECT * FROM pais_A;
SELECT * FROM pais_B;


-- Supongamos que ahora nos damos cuenta que ese valor duplicado lo
-- cargamos por error: no queríamos que fuera  34, sino que debería ser 0
-- Entonces actualizaremos ese valor.

UPDATE pais_B SET Produccion_Autos = '0' WHERE Produccion_Vacas = '121';

-- Observamos que la corrección fue exitosa, pero que los "id" no quedaron
-- ordenados (esto no afecta en nada, pero en el siguiente paso lo ordenaremos)

SELECT * FROM pais_B;


-- Ordenamos la tabla "pais_B" por "id", criterio ascendente (por defecto)

SELECT * FROM pais_B ORDER BY id;


-- Ahora bien, observamos que la última fila de la tabla "pais_B",
-- correspondiente al   "id = 6", tiene valores negativos, lo cual
-- conceptualmente es un error (¿producciones negativas?), por lo que
-- eliminaremos esa fila entera.

DELETE FROM pais_B WHERE Produccion_Vacas = '-850';

-- Observamos ahora la tabla finalmente depurada.

SELECT * FROM pais_B;


-- Por último, podemos ordenar ambas tablas de diferentes maneras y pedir
-- que me de algunos registros y no todos (por ejemplo, solo el primero)

SELECT * FROM pais_A ORDER BY id DESC;
SELECT * FROM pais_B ORDER BY id DESC;

SELECT * FROM pais_A ORDER BY id LIMIT 1;
SELECT * FROM pais_B ORDER BY id LIMIT 1;



-- Finalmente, si quisieramos exportar nuestra base de datos en un
-- archivo.sql, debemos utilizar el siguiente comando en la terminal:

-- pg_dump -U username -h localhost databasename >> sqlfile.sql

-- En nuestro caso particular, lo haríamos de la siguiente manera:

pg_dump -U seba -h localhost fpp >> fpp.sql

-- Recordando que la contraseña de la base es   "123456"


-- pg_dump defaults to plain SQL export. both data and structure.

-- open command prompt and run
-- pg_dump -U username -h localhost databasename >> sqlfile.sql
