from django.db import models

class RegistroAsistencia(models.Model):
    TIPO_DOC_CHOICES = [
        ('', 'Seleccione su tipo de documento'),
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
    ]

    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOC_CHOICES)
    documento = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    fecha = models.DateField()
    asistio = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.fecha}"