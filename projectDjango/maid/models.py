from django.db import models
from customer.models import Maid
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User

# Create your models here.
@receiver(post_save, sender=User)
def create_or_update_maid_profile(sender, instance, created, **kwargs):
    if created:
        Maid.objects.create(user=instance)