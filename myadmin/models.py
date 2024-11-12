from django.db import models

# Create your models here.
class Category(models.Model):
	cname=models.CharField(max_length=50)

	class Meta:
		db_table='category'