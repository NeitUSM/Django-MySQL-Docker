FROM python:3.10-slim

WORKDIR /usr/src/app

RUN pip install --upgrade pip

# Instalar dependencias necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    mariadb-client \
    build-essential \
    && apt-get clean

# Definir ARG para recibir las variables de entorno en tiempo de construcción
ARG DJANGO_PORT
ARG MYSQL_HOST
ARG MYSQL_PORT
ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD

# Convertir ARG en ENV para ser utilizadas en tiempo de ejecución
ENV DJANGO_PORT=$DJANGO_PORT
ENV MYSQL_HOST=$MYSQL_HOST
ENV MYSQL_PORT=$MYSQL_PORT
ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación Django
COPY . .

# Puerto expuesto
EXPOSE ${DJANGO_PORT}

# Comando de inicio
ENTRYPOINT ["sh", "-c", "python wait_for_mysql.py && python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:${DJANGO_PORT}"]