from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    email_verified = models.BooleanField(default=False)
    billing_address = models.CharField(max_length=100,null=True,blank=True)
    delivery_address = models.CharField(max_length=100,null=True,blank=True)
    
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name='profile')
