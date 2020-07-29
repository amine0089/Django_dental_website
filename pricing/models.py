from django.db import models

class Price(models.Model):
	title = models.CharField(max_length=50)
	stage = models.CharField(max_length=25)
	price = models.IntegerField()

	def __str__(self):
 		return self.title
