from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=200)
    headline = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    pub_date = models.DateField(null=True)
    author = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_lines = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.headline

