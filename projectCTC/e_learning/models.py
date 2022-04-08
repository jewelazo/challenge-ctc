from django.db import models

# Create your models here.
class Padre(models.Model):
    name=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=60)
    nacionalidad=models.CharField(max_length=60,blank=True,null=True)
    telefono=models.CharField(max_length=12)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name,self.apellidos)
