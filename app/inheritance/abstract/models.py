from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    school = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}의 학교: {self.school}'


class Instructor(CommonInfo):
    academy = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}의 학원: {self.academy}'
