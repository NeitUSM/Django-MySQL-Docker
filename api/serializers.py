from rest_framework import serializers
from core.models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'titulo', 'fecha_inicio', 'fecha_termino', 'descripcion', 'tipo', 'segmento')
        read_only_fields = ('id', )