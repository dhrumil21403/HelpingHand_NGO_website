from django.db import models
from datetime import date
from django.contrib.auth.models import User
from myadmin.models import Category
from datetime import datetime

# Create your models here.
class Inquiry(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=100)
	contact=models.BigIntegerField()
	message=models.CharField(max_length=100)
	date=models.DateField()

	class Meta:
		db_table='inquiry'

class State(models.Model):
	state_name=models.CharField(max_length=20)

	class Meta:
		db_table='State'

class City(models.Model):
	city_name=models.CharField(max_length=20)
	state=models.ForeignKey(State,on_delete=models.CASCADE,default='')
	class Meta:
		db_table='City'

class Area(models.Model):
	area_name=models.CharField(max_length=12,default='')
	city=models.ForeignKey(City,on_delete=models.CASCADE,default='')

	class Meta:
		db_table='area'

class Role(models.Model):
	role=models.CharField(max_length=20)

	class Meta:
		db_table='role'
		
class Feedback(models.Model):
	ratings=models.CharField(max_length=10)
	comment=models.TextField()
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'feedback'

class Donation(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
	title=models.CharField(max_length=20,default='')
	decoration=models.TextField(max_length=20,default='')
	category=models.ForeignKey(Category,on_delete=models.CASCADE,default='')
	address=models.TextField(max_length=100,default='')
	city=models.ForeignKey(City,on_delete=models.CASCADE,default='')
	area=models.ForeignKey(Area,on_delete=models.CASCADE,default='')
	state=models.ForeignKey(State,on_delete=models.CASCADE,default='')
	date = models.DateField(default=date.today)
	status = models.CharField(max_length=100,default='pending')
	
	class Meta:
		db_table = 'donation'

class Donation_status(models.Model):
	volunteer = models.ForeignKey(User,on_delete=models.CASCADE,default='')
	donation  = models.ForeignKey(Donation, on_delete=models.CASCADE,default='')
	approved_datetime = models.DateTimeField(default=datetime.now)
	approved_remarks = models.TextField(default='')
	received_datetime = models.CharField(max_length=20,default='')
	received_remarks = models.TextField(default='')
	delivered_datetime = models.CharField(max_length=20,default='')
	delivered_remarks = models.TextField(default='')

	class Meta:
		db_table = 'donation_status'


class Donate(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
	amount=models.DecimalField(max_digits=10,decimal_places=2,default='')
	description=models.TextField(max_length=100,default='')
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'donate'

class Requestevents(models.Model):
	title=models.CharField(max_length=20,default='')
	description=models.CharField(max_length=20,default='')
	eventtype=models.CharField(max_length=20,default='')
	user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
	state=models.ForeignKey(State,on_delete=models.CASCADE,default='')
	city=models.ForeignKey(City,on_delete=models.CASCADE,default='')
	area=models.ForeignKey(Area,on_delete=models.CASCADE,default='')
	date = models.DateField(default=date.today)
	status=models.CharField(max_length=20,default='')
	remarks=models.TextField(default='')

	class Meta:
		db_table = 'requestevents'

class Register(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,default='')
	contact=models.BigIntegerField(default='')
	dob=models.CharField(max_length=100,default='')
	address=models.TextField(max_length=100,default='')
	gender=models.CharField(max_length=10,default='')
	city=models.ForeignKey(City,on_delete=models.CASCADE,default='')
	area=models.ForeignKey(Area,on_delete=models.CASCADE,default='')
	role=models.ForeignKey(Role,on_delete=models.CASCADE,default='')
	image=models.CharField(max_length=255,default='')
	date = models.CharField(max_length=100,default='')

	class Meta:
		db_table = 'register'




