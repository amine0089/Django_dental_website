from django.shortcuts import render,redirect
from service.models import Service
from pricing.models import Price
from about.models import Profile
from blog.models import BlogPost 
from .forms import ApointmentForm

def home_v(request):
	services = Service.objects.all()
	pricess = Price.objects.all()
	profiles = Profile.objects.all()
	post_list = BlogPost.objects.all()

	if request.method == 'POST':
		form = ApointmentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ApointmentForm()
	context = {
				'services':services,
				'pricess':pricess,
				'profiles':profiles,
				'post_list':post_list,
				'form':form,
				}
	return render(request,'home/index.html',context)
