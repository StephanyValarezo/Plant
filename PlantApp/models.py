from django.db import models

# Create your models here.


class Botones(models.Model):
    nombre=models.CharField(max_length=30)
    estado=models.BooleanField()
