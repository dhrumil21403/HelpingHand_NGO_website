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
from volunteer import views

urlpatterns = [
     path('layout', views.layout, name='layout'),
     path('dashboard', views.dashboard, name='dashboard'),
     path('alldonation', views.alldonation, name='alldonation'),
     path('viewdetaildonationpost/<int:id>', views.viewdetaildonationpost, name='viewdetaildonationpost'),
     path('donationstatus/<int:id>', views.donationstatus, name='donationstatus'), 
     path('storedonationstatus/<int:id>', views.storedonationstatus, name='storedonationstatus'),
     path('acceptedpost', views.acceptedpost, name='acceptedpost'),
     path('viewdetailaccepteddonation/<int:id>', views.viewdetailaccepteddonation, name='viewdetailaccepteddonation'),
    path('recieved/<int:id>', views.recieved, name='recieved'),
    path('storerecieved/<int:id>', views.storerecieved, name='storerecieved'),
    path('delivered/<int:id>', views.delivered, name='delivered'),
    path('storedelivered/<int:id>', views.storedelivered, name='storedelivered'),
     path('login', views.login, name='login'),
     path('login_check', views.login_check, name='login_check'),
     path('logout', views.logout, name='logout'),
    # path('commontable', views.commontable, name='commontable'),
    # path('allcategory', views.allcategory, name='allcategory'),
    # path('allvolunteer', views.allvolunteer, name='allvolunteer'),
    # path('alluser', views.alluser, name='alluser'),
    # path('allevent', views.allevent, name='allevent'),
    # path('inquiry', views.inquiry, name='inquiry'),
    # path('feedback', views.feedback, name='feedback'),
    # path('commonform', views.commonform, name='commonform'),
    # path('addcategory', views.addcategory, name='addcategory'),
    # path('login', views.login, name='login'),
]

