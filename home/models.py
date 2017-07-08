from django.db import models

# Create your models here.
class Noticia(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 100)
	url = models.CharField(max_length = 200)
	published_date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title
