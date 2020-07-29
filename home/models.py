from django.db import models

SCHELDULE_TYPE =(
		('9 AM to 10 AM','9 AM to 10 AM'),
		('11 AM to 12 AM','11 AM to 12 AM'),
		('2 PM to 4 PM','2 PM to 4 PM'),
		('8 PM to 10 PM','8 PM to 10 PM'),
	)

class Apointment(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	addresse = models.CharField(max_length=50)
	scheldule = models.CharField(max_length=50,choices=SCHELDULE_TYPE)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name='apointment'
		verbose_name_plural='apointments'