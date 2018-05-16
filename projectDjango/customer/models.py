from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
import numpy as np

class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True, blank=True)
	telephone = models.CharField(max_length=10)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

class Maid(models.Model):
	user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True, blank=True)
	image_maid = models.ImageField(upload_to='picmaid',null=True,blank=True)
	address = models.CharField(max_length=100,null=True)
	telephone = models.CharField(max_length=10,null=True)

	def average_rating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return np.mean(all_ratings)

	def __str__(self):
		return self.user.username

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    maid = models.ForeignKey(Maid , on_delete=models.SET_NULL,null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

TYPEAREA_CHOICES=[
	('home', 'Home'),
	('condo', 'Condo'),
]

SIZE_CHOICES = [
	('less25', 'Lessthan 25 sqm.'),
	('between', 'Between 25 to 50 sqm.'),
	('morethan', 'Morethan 50 sqm.'),
]

class Reserve(models.Model):
	reserve_date = models.DateTimeField(default=timezone.now )
	cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	typearea = models.CharField(choices=TYPEAREA_CHOICES, max_length=128, null=True)
	size = models.CharField(choices=SIZE_CHOICES, max_length=128, null=True)
	addresswork = models.CharField(max_length=200,null=True)
	datework = models.DateTimeField(default=timezone.now )
	maid_id = models.ForeignKey("Maid", on_delete=models.SET_NULL, blank=True,null=True)
	user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True, blank=True)
	def __str__(self):
		return "id %s %s"%(self.id,self.maid_id.user.username)

class Money(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True, blank=True)
	resever_id =  models.OneToOneField(Reserve, on_delete=models.SET_NULL,null=True)
	image_slip = models.ImageField(upload_to='slip',null=True)
	timesection = models.DateTimeField(default=timezone.now)
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return self.user.username







