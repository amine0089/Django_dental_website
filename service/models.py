from django.db import models


class Service(models.Model):
	image = models.ImageField(upload_to = 'media/service')
	title = models.CharField(max_length=50)
	text = models.TextField()

	def __str__(self):
		return self.title