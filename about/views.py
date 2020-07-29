from django.shortcuts import render
from .models import Profile
# Create your views here.
def about_us(request):
	profile = Profile.objects.all()
	context = {'profile':profile,}
	return render(request,'about/aboutus.html',context) 