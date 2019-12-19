from django.db import models


class WPSUser(models.Model):
    instructor = models.ForeignKey('self',
                                   related_name='student_set',
                                   on_delete=models.SET_NULL,
                                   null=True)

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
