from django.db import models

# Create your models here.

class Info(models.Model):

    address = models.CharField(max_length=50)
    phone_numper = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.address