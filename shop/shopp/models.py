from django.db import models


class Toifa(models.Model):
    nomi = models.CharField(max_length=50)


class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narx = models.FloatField()
    tarif = models.TextField(null=True)
    soni = models.IntegerField(default=10)
    toifasi = models.ForeignKey(Toifa, on_delete=models.CASCADE)
    rasm = models.ImageField(null=True)


