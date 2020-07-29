from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from slugify import slugify
from taggit.managers import TaggableManager

class BlogPost(models.Model):
	auther = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	description = models.TextField()
	image = models.ImageField(upload_to = 'media/blog')
	created = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey('Category',on_delete = models.SET_NULL,null=True)
	tags = TaggableManager(blank=True)




	def __str__(self):
		return str(self.title)



	class Meta:
		verbose_name='BlogPostss'
		verbose_name_plural='BlogPosts'




class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
