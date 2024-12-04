from django.shortcuts import render
from core.models import Evento
from rest_framework import viewsets, permissions, generics
from .serializers import EventoSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDeveloper

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    permission_classes = [IsAuthenticated, IsDeveloper]
    serializer_class = EventoSerializer

class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def get_queryset(self):
        queryset = Evento.objects.all()
        anio = self.request.query_params.get('anio')
        tipo = self.request.query_params.get('tipo')
        segmento = self.request.query_params.get('segmento')

        if anio:
            queryset = queryset.filter(fecha_inicio__year=anio)
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        if segmento:
            queryset = queryset.filter(segmento=segmento)

        return queryset