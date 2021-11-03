from django.db import models


class Region(models.Model):
    nombre = models.CharField(max_length=90)
    def __str__(self):
      return self.nombre

class Comuna(models.Model):
    nombre =  models.CharField(max_length=90) 
    id_region =  models.ForeignKey(Region, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre 


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    id_region = models.ForeignKey(Comuna, on_delete=models.PROTECT) 
    def __str__(self):
        return self.nombre
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Pago(models.Model):
    tipo = models.CharField(max_length=50)
    id_agenda = models.IntegerField(max_length=11)
    fecha_pago = models.DateField()  
    monto_pago = models.IntegerField(max_length=11)   
def __str__(self):
    return self.tipo 

class Persona(models.Model):
    rut = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre

class Medico(models.Model):
      id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT) 
      id_especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)
def __str__(self):
    return self.id_persona         

class Agenda(models.Model):
    paciente = models.CharField(max_length=50) 
    id_medico =  models.ForeignKey(Medico, on_delete=models.PROTECT)  
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)

    def __str__(self):
        return self.paciente
