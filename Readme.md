Proyecto aplicación web asignatura Taller Lenguaje Programación
----------------------------------------------------
# ¿Qué puede hacer la aplicación?
Se puede crear, modificar, visualizar eventos en un calendario, posee API.
De ser necesario el código podrá ir escalando para completar sus adicionales.

## ¡Importante!
Para el completo funcionamiento de la aplicación web se debe realizar la instalación de las
siguientes dependencias que agregaré posteriormente. Toda la instalación de la dependencia se utiliza el comando pip install

### Dependencias
Las siguientes dependencias estarán asignadas con la versión con la que fue desarrollada la aplicación
1. python3 (3.12.0)
2. django-admin (4.2.7)
3. djangorestframework

## ¿Cómo ejecutar la aplicación web?
1. Clonar y acceder al repositorio.
2. Cargar migración de los modelos (python3 manage.py makemigrations)
3. Migrar los modelos (python3 manage.py migrate)
4. Ejecutar la aplicación web (python3 manage.py runserver)

### ¿Cómo acceder con cuenta de administrador?
Para acceder con cuenta de administrador se debe generar con el comando "python3 manage.py createsuperuser" y rellenar los campos.

## Tecnologías utilizadas
Frontend: HTML5, CSS3 (Bootstrap) y JS.
Backend: Python (Django), API (Django Rest Framework) y SQLITE

Aplicación desarrollada por Matia Zambelli y Natán Apablaza
