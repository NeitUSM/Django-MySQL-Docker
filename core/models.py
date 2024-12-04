from django.db import models
from django.contrib.auth.models import Group

class Evento(models.Model):
    titulo = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.TextField(max_length=255, blank=True)
    segmento = models.ManyToManyField(Group)

    TIPO_CHOICES = [
        ("Vac", "Vacaciones"),
        ("Fer", "Feriado"),
        ("SusAct", "Suspension de Actividades"),
        ("SusActPM", "Suspension de Actividades PM"),
        ("PerLec", "Periodo Lectivo"),
        ("SusEval", "Suspensión de Evaluaciones"),
        ("Cer", "Ceremonia"),
        ("EDDA", "EDDA"),
        ("Eval", "Evaluación"),
        ("Ayu", "Ayudantías"),
        ("HitAca", "Hito Académico"),
        ("SecAca", "Secretaría Académica"),
        ("OAI", "OAI"),
    ]

    tipo = models.CharField(max_length=40, choices=TIPO_CHOICES)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"