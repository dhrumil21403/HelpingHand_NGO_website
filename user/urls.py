"""
URL configuration for helpinghandfinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from user import views

urlpatterns = [
      path('index', views.index, name='index'),
      path('layout', views.layout, name='layout'),
      path('aboutus', views.aboutus, name='aboutus'),
      path('causes', views.causes, name='causes'),
      path('events', views.events, name='events'),
      path('blog', views.blog, name='blog'),
      path('contact', views.contact, name='contact'),
      path('storecontact', views.storecontact, name='storecontact'),
      path('donate', views.donate, name='donate'),
      path('storedonate', views.storedonate, name='storedonate'),
      path('volunteer', views.volunteer, name='volunteer'),
      path('meettheteam', views.meettheteam, name='meettheteam'),
      path('services', views.services, name='services'),
      path('feedback', views.feedback, name='feedback'),
      path('storefeedback', views.storefeedback, name='storefeedback'),
    path('single', views.single, name='single'),
    path('donation', views.donation, name='donation'),
    path('storedonation', views.storedonation, name='storedonation'),
    path('requestevents', views.requestevents, name='requestevents'),
    path('storerequestevents', views.storerequestevents, name='storerequestevents'),
    path('registeruser', views.registeruser, name='registeruser'),
    path('storeregister', views.storeregister, name='storeregister'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('myevents', views.myevents, name='myevents'),
    path('mymoneydonation', views.mymoneydonation, name='mymoneydonation'),
    path('manageprofile', views.manageprofile, name='manageprofile'),
    path('updateregister/<int:id>', views.updateregister, name='updateregister'),
    path('mydonations', views.mydonations, name='mydonations'),
    path('payment_process', views.payment_process, name='payment_process'),
    path('success', views.success, name='success'),
]

