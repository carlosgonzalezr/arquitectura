from django.db import models


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre   


class Agenda(models.Model):

    paciente = models.CharField(max_length=50) 
    medico = models.CharField(max_length=50) 
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)

    def __str__(self):
        return self.paciente

