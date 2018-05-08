from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
User = get_user_model()

class Customer(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
	image = models.ImageField(upload_to='piccustomer',null=True)
	# first_name = models.CharField(max_length=50)
	# last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	postcode = models.CharField(max_length=5)
	telephone = models.CharField(max_length=10)
	# email = models.EmailField(max_length=50)

	def __str__(self):
		return "id: %s %s"%(self.id,self.address)
	


class Maid(models.Model):
	image_maid = models.ImageField(upload_to='picmaid',null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	postcode = models.CharField(max_length=10)
	telephone = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	# idperson = models.CharField(max_length=13)
	def __str__(self):
		return "id: %s, %s %s %s"%(self.id, self.first_name, self.last_name, self.telephone)

TYPEAREA_CHOICES=[
	('home', 'Home'),
	('condo', 'Condo'),
]

SIZE_CHOICES = [
	('less25', 'Less25'),
	('between', 'Between'),
	('morethan', 'Morethan'),
]

class Reserve(models.Model):
	reserve_date = models.DateTimeField(default=timezone.now )
	cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	typearea = models.CharField(choices=TYPEAREA_CHOICES, max_length=128, null=True)
	size = models.CharField(choices=SIZE_CHOICES, max_length=128, null=True)
	datework = models.DateTimeField(default=timezone.now )
	image = models.ImageField(upload_to='slip',null=True)
	maid_id = models.ForeignKey("Maid", on_delete=models.SET_NULL, blank=True,null=True)
	customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True,null=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
	def __str__(self):
		return "id: %s"%(self.id)

class Money(models.Model):
	cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	reserve_id = models.ForeignKey("Reserve", on_delete=models.SET_NULL, blank=True,null=True)



