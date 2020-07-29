from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	phon_number = models.CharField(max_length=20)
	p_image = models.ImageField(upload_to = 'media/profile')
	work_type = models.CharField(max_length=50)

	def __str__(self):
		return str(self.user)
	

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)