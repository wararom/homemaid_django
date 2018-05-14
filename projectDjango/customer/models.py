from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
	# User = get_user_model()

class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True, blank=True)
	telephone = models.CharField(max_length=10)
	# image  models.EmailField(max_length=50)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    # instance.customer.save()


class Maid(models.Model):
	user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True, blank=True)
	image_maid = models.ImageField(upload_to='picmaid',null=True,blank=True)
	address = models.CharField(max_length=100,null=True)
	telephone = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.user.username


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
	addresswork = models.CharField(max_length=200,null=True)
	datework = models.DateTimeField(default=timezone.now )
	maid_id = models.ForeignKey("Maid", on_delete=models.SET_NULL, blank=True,null=True)
	# customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True,null=True)
	user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True, blank=True)
	def __str__(self):
		return "id: %s %s"%(self.id,self.user.username)

class Money(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True, blank=True)
	resever_id =  models.OneToOneField(Reserve, on_delete=models.SET_NULL,null=True)
	image_slip = models.ImageField(upload_to='slip',null=True)
	timesection = models.DateTimeField(default=timezone.now)
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return self.user.username







