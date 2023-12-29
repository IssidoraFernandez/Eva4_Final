from django.db import models

# Create your models here.
class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    personas = models.IntegerField()
    estado = models.BooleanField(default=False)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.correo + ' ' + self.telefono + ' ' + str(self.fecha) + ' ' + str(self.hora) + ' ' + str(self.personas) + ' ' + str(self.estado) + ' ' + self.mensaje


class 