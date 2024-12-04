import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agendausm.settings")
django.setup()

from django.contrib.auth.models import User

# Credenciales del superusuario
username = "admin"
password = "12345"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password)
    print(f"Superusuario '{username}' creado.")
else:
    print(f"Superusuario '{username}' ya existe.")

