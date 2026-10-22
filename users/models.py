from django.db import models

class Rol(models.Model):
    name = models.CharField(max_length=255)
    dateCreate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Users(models.Model):
    names = models.CharField(max_length=100)
    firstLastname = models.CharField(max_length=100)
    SecondLastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) # Usamos EmailField para validación automática
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    size = models.CharField(max_length=5)
    dateBirth = models.DateField()
    photo = models.ImageField(upload_to='usuarios/', default='default.jpg')
    idRol = models.ForeignKey(Rol, on_delete=models.PROTECT, db_column='idRol') # db_column mantiene el nombre original exacto
    createUser = models.DateTimeField(auto_now_add=True)
    updateUser = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.names} ({self.username})"
