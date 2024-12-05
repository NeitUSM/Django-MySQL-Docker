Actualización de Proyecto TLP CER-3
------------------------------------------------------------------------------------------------------
# ¿Qué puede hacer la aplicación?
Este es un proyecto base creado en conjunto donde se puede crear, modificar, 
visualizar eventos en un calendario y posee API. Se ha hecho una actualización que el proyecto corra en
contenedores hechos en Docker.


## ¡Importante!
Para el completo funcionamiento de la aplicación web se debe realizar la instalación de las
siguientes dependencias. Estas, fueron instaladas desde la página oficial de Docker en Ubuntu.

### Dependencias
Las siguientes dependencias estarán asignadas con la versión con la que fue desarrollada la aplicación:
1. **Docker v.27.3.1**
2. **Docker-compose v.1.29.2**

## ¿Cómo ejecutar la aplicación web?
1. Abrir el directorio raíz en la terminal
2. Ejecutar el comando *sudo docker-compose up --build*

### ¿Cómo acceder con cuenta de administrador?
Para acceder con cuenta de administrador, se consideran las siguientes credenciales tipo
-**user: admin**
-**password: 12345**
Estas credenciales pueden ser modificadas desde el archivo **create_superuser.py** antes de
correr el contenedor.

## Tecnologías utilizadas
- **Creación de contenedores**: Docker y Docker-Compose.
- **Contenedor de Base de Datos**: MySQL.
- **Contenedor del proyecto**:
  - **Frontend**:
    - HTML5
    - CSS3 (Bootstrap)
    - JavaScript
  - **Backend**:
    - Python (Django)
    - API (Django Rest Framework)
