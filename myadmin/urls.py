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
from myadmin import views

urlpatterns = [
     path('layout', views.layout, name='layout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('commontable', views.commontable, name='commontable'), 
    path('allvolunteer', views.allvolunteer, name='allvolunteer'),
    path('alluser', views.alluser, name='alluser'),
    path('allevent', views.allevent, name='allevent'),
    path('alldonate', views.alldonate, name='alldonate'),
    path('deletedonate/<int:id>', views.deletedonate, name='deletedonate'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('deleteinquiry/<int:id>', views.deleteinquiry, name='deleteinquiry'),
    path('feedback', views.feedback, name='feedback'),
    path('deletefeedback/<int:id>', views.deletefeedback, name='deletefeedback'),
    path('commonform', views.commonform, name='commonform'),
    path('addcategory', views.addcategory, name='addcategory'),
    path('storecategory', views.storecategory, name='storecategory'),
    path('allcategory', views.allcategory, name='allcategory'),
    path('deletecategory/<int:id>', views.deletecategory, name='deletecategory'),
    path('editcategory/<int:id>', views.editcategory, name='editcategory'),
    path('updatecategory/<int:id>', views.updatecategory, name='updatecategory'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('addstate', views.addstate, name='addstate'),
    path('storestate', views.storestate, name='storestate'),
    path('allstate', views.allstate, name='allstate'),
    path('deletestate/<int:id>', views.deletestate, name='deletestate'),
    path('addcity', views.addcity, name='addcity'),
    path('storecity', views.storecity, name='storecity'),
    path('allcity', views.allcity, name='allcity'),
    path('deletecity/<int:id>', views.deletecity, name='deletecity'), 
    path('addarea', views.addarea, name='addarea'),
    path('storearea', views.storearea, name='storearea'),
    path('allarea', views.allarea, name='allarea'),
    path('deletearea/<int:id>', views.deletearea, name='deletearea'),
    path('editarea/<int:id>', views.editarea, name='editarea'), 
    path('updatearea/<int:id>', views.updatearea, name='updatearea'),
    path('addroles', views.addroles, name='addroles'),
    path('storeroles', views.storeroles, name='storeroles'),
    path('viewdetailuser/<int:id>', views.viewdetailuser, name='viewdetailuser'),
    path('viewdetailvolunteer/<int:id>', views.viewdetailvolunteer, name='viewdetailvolunteer'),
    path('logout', views.logout, name='logout'),
    path('viewdetailevent/<int:id>', views.viewdetailevent, name='viewdetailevent'),
    path('acceptreject/<int:id>', views.acceptreject, name='acceptreject'),
    path('storeacceptreject/<int:id>', views.storeacceptreject, name='storeacceptreject'),
    path('alldonation', views.alldonation, name='alldonation'),
    path('viewdetaildonation/<int:id>', views.viewdetaildonation, name='viewdetaildonation'),
    path('viewvolunteer/<int:id>', views.viewvolunteer, name='viewvolunteer'),
    path('viewuser/<int:id>', views.viewuser, name='viewuser'),
]

