# DAS_FINAL_PROJECT
Repositorio para el proyecto final de la materia Diseño y Arqitectura de Software.

## MATERIA
Diseño y Arquitectura de Software.

## Profesor
Ing. Angel Santiago Jaime Zavala.

## Equipo
- Angela Gabriela Sanchez Niño.
- Emilio Barrera Gonzalez.
- Juan de Dios Almaguer Constante.
- Luis Fernando Garcia Morales.

## Prerequisitos
- Docker.

## Tecnologias
- Python (flask, peewee).
- Docker, Docker-Compose.
- Redis.
- PostgreSQL.
- Pgadmin.
- Materialize.

## Introducción
Con este proyecto se busca demostrar que los conocimientos del profesor han sido transferidos correctamente hacia el alumno.
Se utilizarán las tecnologías que se manejaron a lo largo del ciclo escolar.

## Descripción
Utilizando las tecnlogías mencionadas anteriormente, hay que construir una serie de contenedores de **Docker** conectados entre si para servir una aplicación implementada con **Python** que mostrara una lista de heroes de DC Comics & , utilizando *flask* como framework web y *peewee* como ORM, alimentada con una base de datos de **PostgreSQL** que puede ser optimizada con la imagen de **pgAdmin** incluida en el *docker-compose*. Adicionalmente, se implementa un contenedor con **Redis** para encargarse de cache generado por la base de datos para agilizar las consultas a la base de datos.  
Utilizamos **Materialize** como framework para el CSS de la aplicación web. 

## Instrucciones
1. Clonar o descargar el repositorio.<br>
En caso de que lo hayas descargado, tambien hay que extraerlo.
2. Entrar a la carpeta del reposositorio y abrir una terminal en ella.
3. Detener los contenedores.  

<code>$ docker kill [container id]</code>

4. Eliminar las Imagenes.<br>
Para prevenir problemas, si sabes lo que estas haciendo puedes saltar este paso.

<code>$ docker system prune -a</code>

5. Correr los contenedores.

<code>$ docker-compose up --build</code>

Nota: Una vez que este corriendo podremos ver en consola lo que esta ocurriendo,tomará bastante tiempo, pero hay que esperar a que aparezca en pantalla el mensaje "dc_script exited with a code 0".

6. Acceder a http://0.0.0.0:5000 para ver la app, o http://0.0.0.0:5050 para acceder al pgadmin.

<code>correo: pgadmin4@pgadmin.org</code>  
<code>contraseña: admin</code>

7. Para detener la Ejecución hay que presionar <kbd>CTRL</kbd> + <kbd>C</kbd> y esperar a que los contenedores se detengan

Nota: Puede forzarce la detención de los contenedores si durante el proceso de detención "graciosa" se vuelve a presionar <kbd>CTRL</kbd> + <kbd>C</kbd>


## Agradecimientos
- Al Profesor Angel Santiago Jaime Zavala por brindarnos atención dentro y fuera de la clase aún dentro de estos tiempos tan complicados y por enseñarnos tecnologías de punta de lanza.
- Al equipo por la dedicación al proyecto.
- A nuestras familias por su comprensión y apoyo a lo largo del proyecto.
