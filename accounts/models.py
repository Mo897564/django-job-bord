from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    city = models.ForeignKey(City , on_delete=models.CASCADE , blank=True, null=True)
    phone = models.CharField(max_length=50 , null=True , blank=True)
    img = models.ImageField(upload_to= 'photos/profile/%y/%m/%d' , default= 'photo_default/profile.png')
    bio = models.TextField(max_length=2000 , null=True, blank=True)

    def __str__(self):
        return self.user.username