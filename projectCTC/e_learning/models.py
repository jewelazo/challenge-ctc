from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

SEX_OPTIONS = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('T', 'They')
)

# Create your models here.
class Padre(models.Model):
    name=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=60,blank=True,null=True)
    genero=models.CharField(max_length=1, choices=SEX_OPTIONS)
    edad=models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(100)])
    email=models.EmailField(max_length=70,blank=True,null=True,unique=True)
    telefono=models.CharField(max_length=12)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name,self.apellidos)

class Estudiante(models.Model):
    name=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=60,blank=True,null=True)
    genero=models.CharField(max_length=1, choices=SEX_OPTIONS)
    edad=models.IntegerField(validators=[MinValueValidator(5),MaxValueValidator(17)])
    padre=models.ForeignKey(Padre, on_delete=models.CASCADE)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name,self.apellidos)

class Curso(models.Model):
    name=models.CharField(max_length=100,unique=True)
    precio=models.DecimalField(max_digits=5,decimal_places=2)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.name)


class Matricula(models.Model):
    curso=models.ForeignKey(Curso,on_delete=models.PROTECT)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    creado=models.DateTimeField(auto_now_add=True)
    editado=models.DateTimeField(auto_now=True)