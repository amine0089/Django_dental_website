
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace = 'home')),
    path('service/',include('service.urls',namespace = 'service')),
    path('blog/',include('blog.urls',namespace = 'blog')),
    path('pricing/',include('pricing.urls',namespace = 'pricing')),
    path('aboutus/',include('about.urls',namespace = 'about')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)