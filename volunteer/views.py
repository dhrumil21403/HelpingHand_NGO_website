from django.shortcuts import render,redirect
from user.models import Register,Donation,Donation_status
from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.
def layout(request):
	context={}
	return render(request,'volunteer/common/layout.html',context)
def dashboard(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	context={'profile':profile}
	return render(request,'volunteer/dashboard.html',context)
def alldonation(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation.objects.filter(status='pending')
	context={'result':result,'profile':profile}
	return render(request,'volunteer/alldonation.html',context)

def viewdetaildonationpost(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'volunteer/viewdetaildonationpost.html',context)

def donationstatus(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'volunteer/donationstatus.html',context)

def storedonationstatus(request,id):
	user_id=request.user.id
	myremark = request.POST['remark']
	mystat = request.POST['statuss']
	result=Donation.objects.get(pk=id)
	data={'status':mystat}
	Donation.objects.update_or_create(pk=id,defaults=data)
	Donation_status.objects.create(approved_remarks=myremark,volunteer_id=user_id,donation_id=result.id)
	return redirect('/volunteer/alldonation')

def viewdetailaccepteddonation(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'volunteer/viewdetailaccepteddonation.html',context)

def recieved(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation_status.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'volunteer/recieved.html',context)

def storerecieved(request,id):
	mydatetime = request.POST['datetime']
	myremark = request.POST['remark']
	data={
	'received_datetime':mydatetime,'received_remarks':myremark
	}
	Donation_status.objects.update_or_create(pk=id,defaults=data)
	return redirect('/volunteer/acceptedpost')

def delivered(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation_status.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'volunteer/delivered.html',context)

def storedelivered(request,id):
	mydatetime = request.POST['datetime']
	myremark = request.POST['remark']
	data={
	'delivered_datetime':mydatetime,'delivered_remarks':myremark
	}
	Donation_status.objects.update_or_create(pk=id,defaults=data)
	return redirect('/volunteer/acceptedpost')

def login(request):
	context={}
	return render(request,'volunteer/login.html',context)

def login_check(request):
	myusername=request.POST['username']
	mypassword=request.POST['password']

	result=auth.authenticate(username=myusername,password=mypassword)
	if result is None:
		messages.success(request, "Invalid username or password")
		return redirect('/volunteer/login')
	else:
		auth.login(request,result)
		return redirect('/volunteer/dashboard')

def logout(request):
	auth.logout(request)
	return redirect('/volunteer/login')

def acceptedpost(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation_status.objects.filter(volunteer_id=user_id)
	context={'result':result,'profile':profile}
	return render(request,'volunteer/acceptedpost.html',context)