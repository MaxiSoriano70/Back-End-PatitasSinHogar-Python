from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    fechaDeNacimiento = models.DateField()
    email = models.EmailField(max_length=254, unique=True)
    contrasenia = models.CharField(max_length=255)

class Mascota(models.Model):
    nombre = models.CharField(max_length=45)
    urlFoto = models.CharField(max_length=255)
    urlUbicacion = models.CharField(max_length=255)
    fechaDeNacimiento = models.DateField()
    especie = models.CharField(max_length=45)
    colorDePelo = models.CharField(max_length=100)
    pesoKg = models.FloatField()
    isEsterilizado = models.BooleanField()
    observaciones = models.CharField(max_length=250)
    isAdoptado = models.BooleanField(default=False)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Adopcion(models.Model):
    idMascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fechaDeAdopcion = models.DateField(auto_now_add=True)
    nombreAdoptante = models.CharField(max_length=45)
    apellidoAdoptante = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    calle = models.CharField(max_length=45)
    numero = models.IntegerField()
    localidad = models.CharField(max_length=45)
    provincia = models.CharField(max_length=45)
