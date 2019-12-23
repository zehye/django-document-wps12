from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # 역방향 참조는 기본적으로 지원해주지만 필요없는 경우 related_name = '+'를 해주면 역방향참조가 되지 않는다.
    name = models.CharField('차 이름', max_length=100)

    def __str__(self):
        return self.name
