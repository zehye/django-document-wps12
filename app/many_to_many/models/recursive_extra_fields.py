from django.db import models


class FacebookUser(models.Model):
    name = models.CharField(max_length=20)
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.name


class InstagramUser(models.Model):
    name = models.CharField(max_length=20)

    following = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,  # 대칭 = False
        related_name='followers',
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    me = models.ForeignKey(
        InstagramUser, on_delete=models.CASCADE,
        related_name='following_relation_set',
    )
    counterpart = models.ForeignKey(
        InstagramUser, on_delete=models.CASCADE,
        related_name='follower_relation_set',
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Relation (me): {self.me.name} (counterpart): {self.counterpart.name}'



