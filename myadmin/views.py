from django.shortcuts import render,redirect
from myadmin.models import Category
from user.models import Inquiry,City,Area,Role,Feedback,State,Donate,Requestevents,Register,Donation,Donation_status
from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.

def layout(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	context={'profile':profile}
	return render(request,'myadmin/common/layout.html',context)
def dashboard(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	context={'profile':profile}
	# context={}
	return render(request,'myadmin/dashboard.html',context)

def commontable(request):
	context={}
	return render(request,'myadmin/commontable.html',context)

def allvolunteer(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	register=Register.objects.filter(role_id=2)
	context={'register':register,'profile':profile}
	return render(request,'myadmin/allvolunteer.html',context)
	
def alluser(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id) 
	register=Register.objects.filter(role_id=1)
	context={'register':register,'profile':profile}
	return render(request,'myadmin/alluser.html',context)

def allevent(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id) 
	result=Requestevents.objects.all()
	context={'result':result,'profile':profile}
	return render(request,'myadmin/allevent.html',context)

def alldonate(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donate.objects.all()
	context={'result':result,'profile':profile}
	return render(request,'myadmin/alldonate.html',context)

def deletedonate(request,id):
	result=Donate.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/alldonate')

def feedback(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id) 
	result=Feedback.objects.all()
	context={'result':result,'profile':profile}
	return render(request,'myadmin/feedback.html',context)
	
def deletefeedback(request,id):
	result=Feedback.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/feedback')

def commonform(request):
	context={}
	return render(request,'myadmin/commonform.html',context)

def login(request):
	context={}
	return render(request,'myadmin/login.html',context)

def login_check(request):
	myusername=request.POST['username']
	mypassword=request.POST['password']

	result=auth.authenticate(username=myusername,password=mypassword)
	if result is None:
		messages.success(request, "Invalid username or password")
		return redirect('/myadmin/login')
	else:
		auth.login(request,result)
		return redirect('/myadmin/dashboard')


#Categorycrud
def addcategory(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)	
	context={'profile':profile}
	return render(request,'myadmin/addcategory.html',context)

def storecategory(request):
	mycname=request.POST['cname']
	Category.objects.create(cname=mycname)
	return redirect('/myadmin/addcategory')

def allcategory(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Category.objects.all()
	context={'result':result,'profile':profile}
	return render(request,'myadmin/allcategory.html',context)

def deletecategory(request,id):
	result=Category.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/allcategory')

def editcategory(request,id):
	result=Category.objects.get(pk=id)
	context={'result':result}
	return render(request,'myadmin/editcategory.html',context)

def updatecategory(request,id):
	mycname=request.POST['cname']
	data={'cname':mycname }
	Category.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/allcategory')
# inquirycrud
def inquiry(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Inquiry.objects.all()
	context={'result':result,'profile':profile}
	return render(request,'myadmin/inquiry.html',context)

def deleteinquiry(request,id):
	result=Inquiry.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/inquiry')

def addstate(request):
	context={}
	return render(request,'myadmin/addstate.html',context)

def storestate(request):
	mystatename=request.POST['statename']
	State.objects.create(state_name=mystatename)
	return redirect('/myadmin/addstate')

def allstate(request):
	result=State.objects.all()
	context={'result':result}
	return render(request,'myadmin/allstate.html',context)

def deletestate(request,id):
	result=State.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/allstate')

def addcity(request):
	result=State.objects.all()
	context={'state':result}
	return render(request,'myadmin/addcity.html',context)

def storecity(request):
	mycityname=request.POST['cityname']
	mystate=request.POST['statename']
	City.objects.create(city_name=mycityname,state_id=mystate)
	return redirect('/myadmin/addcity')

def allcity(request):
	result=City.objects.all()
	context={'result':result}
	return render(request,'myadmin/allcity.html',context)

def deletecity(request,id):
	result=City.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/allcity')

def addarea(request):
	result=City.objects.all()
	context={'city':result}
	return render(request,'myadmin/addarea.html',context)

def storearea(request):
	myareaname=request.POST['areaname']
	mycity=request.POST['cityname']
	Area.objects.create(area_name=myareaname,city_id=mycity)
	return redirect('/myadmin/addarea')

def allarea(request):
	result=Area.objects.all()
	context={'result':result}
	return render(request,'myadmin/allarea.html',context)

def deletearea(request,id):
	result=Area.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/allarea')

def editarea(request,id):
	result1=City.objects.all()
	result=Area.objects.get(pk=id)
	context={'result':result,'city':result1}
	return render(request,'myadmin/editarea.html',context)

def updatearea(request,id):
	myareaname=request.POST['areaname']
	mycity=request.POST['cityname']
	data={'area_name':myareaname,
		  'city_id':mycity,	  	
		}
	Area.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/allarea')

def addroles(request):
	context={}
	return render(request,'myadmin/addrole.html',context)

def storeroles(request):
	myrole=request.POST['role']
	Role.objects.create(role=myrole)
	return redirect('/myadmin/addroles')

def viewdetailuser(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Register.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'myadmin/viewdetailuser.html',context)

def viewdetailvolunteer(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Register.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'myadmin/viewdetailvolunteer.html',context)

def viewdetailevent(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Requestevents.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'myadmin/viewdetailevent.html',context)

def logout(request):
	auth.logout(request)
	return redirect('/myadmin/login')

def acceptreject(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Requestevents.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'myadmin/acceptreject.html',context)

def storeacceptreject(request,id):
	mystatus  = request.POST['status']
	myremark = request.POST['remark']
	data={
	'status':mystatus,'remarks':myremark
	}

	Requestevents.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/allevent')

def alldonation(request):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation_status.objects.all()
	context={'result':result,'profile':profile}
	return render(request,'myadmin/alldonation.html',context)

def viewdetaildonation(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation_status.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'myadmin/viewdetaildonation.html',context)

def viewvolunteer(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation_status.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'myadmin/viewvolunteer.html',context)

def viewuser(request,id):
	user_id=request.user.id
	profile=Register.objects.get(user_id=user_id)
	result=Donation_status.objects.get(pk=id)
	context={'result':result,'profile':profile}
	return render(request,'myadmin/viewuser.html',context)