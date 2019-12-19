from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField('차 이름', max_length=100)

    def __str__(self):
        return self.name
