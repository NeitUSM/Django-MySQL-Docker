import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .models import Evento
from django.contrib.auth import logout

# Create your views here.
def Home(request):
    filtrar_segmento = request.GET.get('Segmento')
    filtrar_tipo = request.GET.get('Tipo')

    opciones_unicas = set()

    grupos = Group.objects.all()
    events = Evento.objects.all()
    lista_eventos = []
    lista_tupla = []

    for evento in events:
        tipo_value = evento.tipo
        for opcion_value, opcion_display in Evento.TIPO_CHOICES:
            if tipo_value == opcion_value:
                lista_eventos.append(opcion_display)
                tupla = (opcion_value, opcion_display)
                opciones_unicas.add(tupla)
                break

    # Filtra eventos según el grupo seleccionado
    eventos_segmento = Evento.objects.all().order_by('-fecha_inicio')
    if filtrar_segmento and filtrar_segmento != "Segmento":
        eventos_segmento = eventos_segmento.filter(
            segmento=grupos.get(name=filtrar_segmento)
        )

    # Filtra eventos según el tipo seleccionado
    eventos_tipo = eventos_segmento
    if filtrar_tipo and filtrar_tipo != "Tipo":
        eventos_tipo = eventos_tipo.filter(
            tipo=filtrar_tipo
        )

    eventos = eventos_tipo
    lista_tupla = list(opciones_unicas)

    eventopasado = request.POST.get("eventopasado")
    print("Valor de eventopasado en POST:", eventopasado)
    fecha_actual = datetime.datetime.now()
    if eventopasado == "Algunos":
        eventos = Evento.objects.filter(fecha_termino__gt=fecha_actual).order_by('-fecha_inicio')

    data = {
        'title': filtrar_segmento,
        'eventos': eventos,
        'filtrar_segmento': filtrar_segmento,
        'filtrar_tipo': filtrar_tipo,
        'lista_eventos': lista_eventos,
        'lista_tupla': lista_tupla,
        'grupos': grupos,

    }

    return render(request, 'core/userNoLog.html', data)

def logout_view(request):
    logout(request)
    return redirect('home')