from django.db import models
from users.models import Users 
class PublicationStatus(models.Model):
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.state

class Publication(models.Model):
    TYPE_CHOICES = [
        ('Venta', 'Venta'),
        ('Intercambio', 'Intercambio'),
    ]
    description = models.TextField(blank=True, null=True)
    idStatus = models.ForeignKey(PublicationStatus, on_delete=models.PROTECT, db_column='idStatus')
    typePublication = models.CharField(max_length=20, choices=TYPE_CHOICES)
    datePublication = models.DateTimeField(auto_now_add=True)
    idUser = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='idUser')

    def __str__(self):
        return f"Publicación {self.id} - {self.typePublication}"

class Garment(models.Model):
    garment = models.CharField(max_length=100)
    desciption = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=10)
    firstPhoto = models.ImageField(upload_to='prendas/', blank=True, null=True)
    secondPhoto = models.ImageField(upload_to='prendas/', blank=True, null=True)
    thirdPhoto = models.ImageField(upload_to='prendas/', blank=True, null=True)
    fourthPhoto = models.ImageField(upload_to='prendas/', blank=True, null=True)
    value = models.IntegerField()
    idPublication = models.ForeignKey(Publication, on_delete=models.CASCADE, db_column='idPublication')

    def __str__(self):
        return self.garment
