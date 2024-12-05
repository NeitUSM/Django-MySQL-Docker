import os
import time
import socket

def wait_for_mysql():
    # Obtener las variables de entorno
    host = os.getenv("MYSQL_HOST")
    port = os.getenv("MYSQL_PORT")
    
    # Validar que las variables de entorno existen
    if not host or not port:
        raise ValueError("MYSQL_HOST y MYSQL_PORT deben estar definidos en las variables de entorno.")

    # Intentar conectarse al servidor MySQL
    max_attempts = 60  # Máximo de intentos (1 minuto de espera)
    attempt = 0
    while attempt < max_attempts:
        try:
            with socket.create_connection((host, int(port)), timeout=5):
                print(f"Conexión a MySQL exitosa en {host}:{port}")
                return
        except (socket.timeout, socket.error):
            print(f"Esperando a MySQL en {host}:{port}... Intento {attempt + 1}/{max_attempts}")
            time.sleep(20)
            attempt += 1
    
    raise TimeoutError(f"No se pudo conectar a MySQL en {host}:{port} después de {max_attempts} intentos.")

if __name__ == "__main__":
    wait_for_mysql()