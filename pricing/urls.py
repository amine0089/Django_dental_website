from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('', views.pricing_us, name = 'pricing_us'),
]
