"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view
from django.conf.urls import url # will be able to define what we are expecting from the browser and how to deal with it
from firstpage.views import index_view, predictMPG_view

from products import views
from pages import views 
from firstpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', views.index),
    path('home/', home_view),
    path('contact/', contact_view),
    path('about/', about_view),
    url('^$', index_view, name = 'Homepage'), #this is the default page 
    url('predictMPG', predictMPG_view, name = 'predictMPG')
]
