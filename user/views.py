# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
import os
from django.contrib import messages,auth
from django.contrib.auth.models import User
from user.models import Inquiry,Feedback,City,Area,State,Donate,Requestevents,Role,Register,Donation
from myadmin.models import Category
from django.conf import settings
from datetime import date
import razorpay
from django.views.decorators.csrf import csrf_exempt


def payment_process(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = int(request.session['price'])*100

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"OIBP",
        "notes":{
            'name' : 'AK',
            'payment_for':'OIBP Test'
        }
    }
    id = request.user.id
    result = User.objects.get(pk=id)
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result}
    return render(request, 'user/payment_process.html',context)

@csrf_exempt
def success(request):
	context = {}
	return render(request,'user/success.html',context)




# Create your views here.
def index(request):
	context={}
	return render(request,'user/index.html',context)
def layout(request):
	context={}
	return render(request,'user/common/layout.html',context)
def aboutus(request):
	context={}
	return render(request,'user/aboutus.html',context)
def causes(request):
	context={}
	return render(request,'user/causes.html',context)
def events(request):
	context={}
	return render(request,'user/events.html',context)
def blog(request):
	context={}
	return render(request,'user/blog.html',context)
def donate(request):
	context={}
	return render(request,'user/donate.html',context)

def storedonate(request):
	user_id = request.user.id
	myamount=request.POST['amount']
	mydescription=request.POST['description']
	request.session['price'] = myamount
	Donate.objects.create(user_id=user_id,amount=myamount,description=mydescription)
	return redirect('/user/payment_process')

def volunteer(request):
	context={}
	return render(request,'user/volunteer.html',context)
def meettheteam(request):
	context={}
	return render(request,'user/meettheteam.html',context)
def services(request):
	context={}
	return render(request,'user/services.html',context)
def single(request):
	context={}
	return render(request,'user/single.html',context)
# project
def contact(request):
	context={}
	return render(request,'user/contact.html',context)

def storecontact(request):
	myname=request.POST['name']
	myemail=request.POST['email']
	mycontact=request.POST['contact']
	mymessage=request.POST['message']
	mydate=date.today()
	Inquiry.objects.create(name=myname,email=myemail,contact=mycontact,message=mymessage,date=mydate)
	return redirect('/user/contact')

def feedback(request):
	context={}
	return render(request,'user/feedback.html',context)

def storefeedback(request):
	myratings  = request.POST['ratings']
	mycomment = request.POST['comment']
	user_id = request.user.id

	Feedback.objects.create(ratings=myratings,comment=mycomment,user_id=user_id)
	return redirect('/user/feedback')

def donation(request):
	category=Category.objects.all()
	city=City.objects.all()
	area=Area.objects.all()
	state=State.objects.all()
	context={'category':category,
			'city':city,
			'area':area,
			'state':state,}
	return render(request,'user/donation.html',context)

def storedonation(request):
	user_id = request.user.id
	mytitle=request.POST['title']
	mydecoration=request.POST['decoration']
	mycategory=request.POST['category']
	myaddress=request.POST['address']
	mycity=request.POST['city']
	mystate=request.POST['state']
	myarea=request.POST['area']
	Donation.objects.create(title=mytitle,decoration=mydecoration,category_id=mycategory,address=myaddress,city_id=mycity,area_id=myarea,state_id=mystate,user_id=user_id)
	return redirect('/user/donation')

def requestevents(request):
	state=State.objects.all()
	city=City.objects.all()
	area=Area.objects.all()
	context={'state':state,'city':city,'area':area}
	return render(request,'user/requestevents.html',context)

def storerequestevents(request):
	mytitle=request.POST['title']
	mydescription=request.POST['description']
	user_id = request.user.id
	mystate=request.POST['state']
	mycity=request.POST['city']
	myarea=request.POST['area']
	myeventtype=request.POST['eventtype']
	Requestevents.objects.create(title=mytitle,description=mydescription,user_id=user_id,state_id=mystate,city_id=mycity,area_id=myarea,eventtype=myeventtype)
	return redirect('/user/requestevents')


def login(request):
	context={}
	return render(request,'user/login.html',context)

def registeruser(request):
	city=City.objects.all()
	area=Area.objects.all()
	role=Role.objects.all()
	context={'city':city,'role':role,'area':area}
	return render(request,'user/registeruser.html',context)

def storeregister(request):
	# auth_user
	myfname=request.POST['fname']
	mylname=request.POST['lname']
	myusername=request.POST['username']
	myemail=request.POST['email']
	mypassword=request.POST['password']
	mycpassword=request.POST['cpassword']

	# /register
	mydob=request.POST['dob']
	mycontact=request.POST['contact']
	myaddress=request.POST['address']
	mygender=request.POST['gender']
	mycity=request.POST['city']
	myarea=request.POST['area']
	myrole=request.POST['role']
	myfile = request.FILES['f']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(myfile.name,myfile)
	mydate=date.today()
	if mypassword == mycpassword:
		result=User.objects.create_user(first_name=myfname,last_name=mylname,email=myemail,username=myusername,password=mypassword)
		Register.objects.create(contact=mycontact,address=myaddress,dob=mydob,gender=mygender,city_id=mycity,area_id=myarea,image=myfile.name,role_id=myrole,user_id=result.id,date=mydate)
		return redirect('/user/registeruser')

	else:
		messages.success(request,"Missmatch Password")
		return redirect('/user/registeruser')

def login_check(request):
	myusername=request.POST['username']
	mypassword=request.POST['password']

	result=auth.authenticate(username=myusername,password=mypassword)
	if result is None:
		messages.success(request, "Invalid username or password")
		return redirect('/user/login')
	else:
		auth.login(request,result)
		return redirect('/user/index')

def logout(request):
	auth.logout(request)
	return redirect('/user/login')

def mydonations(request):
	user_id=request.user.id
	result=Donation.objects.filter(user_id=user_id)
	context={'result':result}
	return render(request,'user/mydonation.html',context)

def myevents(request):
	user_id=request.user.id
	result=Requestevents.objects.filter(user_id=user_id)
	context={'result':result}
	return render(request,'user/myevents.html',context)

def mymoneydonation(request):
	user_id=request.user.id
	result=Donate.objects.filter(user_id=user_id)
	context={'result':result}
	return render(request,'user/mymoneydonation.html',context)


def manageprofile(request):
	user_id=request.user.id
	result=Register.objects.get(user_id=user_id)
	city=City.objects.all()
	area=Area.objects.all()
	role=Role.objects.all()
	context={'city':city,'role':role,'area':area,'result':result}
	return render(request,'user/manageprofile.html',context)

def updateregister(request,id):
	# auth_user
	myfname=request.POST['fname']
	mylname=request.POST['lname']
	myusername=request.POST['username']
	myemail=request.POST['email']
	

	# /register
	mydob=request.POST['dob']
	mycontact=request.POST['contact']
	myaddress=request.POST['address']
	mygender=request.POST['gender']
	mycity=request.POST['city']
	myarea=request.POST['area']
	myrole=request.POST['role']
	myfile = request.FILES['f']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(myfile.name,myfile)
	mydate=date.today()
	data={
	'first_name':myfname,
	'last_name':mylname,
	'email':myemail,
	'username':myusername,

	'gender':mygender,
	'dob':mydob,
	'contact':mycontact,
	'address':myaddress,
	'city_id':mycity,
	'area_id':myarea,
	'role_id':myrole,
	'image':myfile.name,
	'date':mydate
	}
	user_id=request.user.id
	User.objects.update_or_create(pk=user_id,defaults=data)
	Register.objects.update_or_create(pk=id,defaults=data)
	return redirect('/user/registeruser')