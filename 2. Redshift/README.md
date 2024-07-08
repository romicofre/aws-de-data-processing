# Contenido

## Código Python

Para conectarse a redshift y realizar algunas operaciones:

### copy_from_s3.py

Script que crea una conexión en la función **create_conn** y luego ejecuta una query, 
la query es una copia de un archivo que ya existe previamente en un bucket de s3.

### file_to_redshift

Carpeta que contiene lo necesario para crear una función lambda.

**Archivo.zip** Se almacena en s3 y luego se crea una función lambda usando este código fuente
en formato zip almacenado en s3.
Las variables de entorno son:
    AWS_RS_DB_NAME
    AWS_RS_DB_HOST
    AWS_RS_DB_PORT
    AWS_RS_DB_USER
    AWS_RS_DB_PASS
    AWS_ACCES_KEY_ID
    AWS_SECRET_ACCES_KEY

**lambda_function.py** Transformación del archivo _copy_from_s3.py_, para poder ejecutarlo en 
una función lambda, pero realiza la misma tarea. Es necesario incluirlo con la biblioteca,
ya que no está incluida en el ambiente de la lambda function.

**psycopg2** Carpeta con archivos de la librería psycopg2, que se usa para crear conexiones a la base de datos.
Es necesario agregarla manualmente a la función lambda, se puede agregar dentro del archivo zip, junto al código 
que la utiliza.

## Código SQL 

### test_movie_from_s3.sql
Crea una tabla y carga datos de un archivo previamente cargado en s3.

### know_errors.sql
Ejemplo de una consulta para obtener el error o los errores de las ejecuciones de queries fallidas.

### create_and_insert.sql
Crea una tabla e inserta datos existentes en otra tabla. Muy útil para realizar limpieza y transformaciones.


# UPDATE
Layers with psycopg2.
Need main code, in lambda handler and create layer with ARN from:
https://github.com/jetbridge/psycopg2-lambda-layer
