from django.db import models

# Create your models here.


class Noticia(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, primary_key=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
