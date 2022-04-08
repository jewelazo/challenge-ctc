from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Padre(models.Model):
    name=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=60,blank=True,null=True)
    edad=models.IntegerField(max_length=2,validators=[MinValueValidator(18)])
    telefono=models.CharField(max_length=12)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name,self.apellidos)

class Estudiante(models.Model):
    name=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=60,blank=True,null=True)
    edad=models.IntegerField(max_length=2,validators=[MinValueValidator(5)])
    padre=models.ForeignKey(Padre, on_delete=models.CASCADE)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name,self.apellidos)

