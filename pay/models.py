from django.db import models
from users.models import Users
from publications.models import Publication

class PaymentMethod(models.Model):
    method = models.CharField(max_length=200)

    def __str__(self):
        return self.method

class PaymentStatus(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Pay(models.Model):
    idUser = models.ForeignKey(Users, on_delete=models.PROTECT, db_column='idUser')
    idPublication = models.ForeignKey(Publication, on_delete=models.PROTECT, db_column='idPublication')
    amount = models.IntegerField()
    idMethod = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, db_column='idMethod')
    idStatus = models.ForeignKey(PaymentStatus, on_delete=models.PROTECT, db_column='idStatus')
    datePay = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id} - ${self.amount}"
