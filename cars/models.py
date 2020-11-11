from django.db import models
from PIL import Image
# Create your models here.
class Cars(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=40,null=True)
    year=models.DateField()
    manufactuer=models.TextField(max_length=40,null=True)
    image=models.ImageField(default='default.jpg',upload_to='image', null=True, blank=True)

class Manufactuers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=40,null=True)
    country=models.TextField(max_length=40,null=True)
    logo=models.ImageField(default='default_logo.jpg',upload_to='logo', null=True, blank=True)
