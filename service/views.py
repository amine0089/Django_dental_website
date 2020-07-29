from django.shortcuts import render
from .models import Service
from blog.models import BlogPost

def service_us(request):
	services = Service.objects.all()
	post_list = BlogPost.objects.all()
	context = {'services':services,
				'post_list':post_list,
				}
	return render(request,'service/services.html',context)