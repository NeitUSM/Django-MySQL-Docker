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


# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación Django
COPY . .

# Puerto expuesto
EXPOSE 8000

# Comando de inicio
CMD ["sh", "-c", "sleep 350 && python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"]

