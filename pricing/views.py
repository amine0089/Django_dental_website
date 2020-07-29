from django.shortcuts import render
from .models import Price
def pricing_us(request):
	prices = Price.objects.all()
	context = {'prices':prices,}
	return render(request,'pricing/price.html',context)
