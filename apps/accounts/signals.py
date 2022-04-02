from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  

from apps.cart.models import Cart
from apps.accounts.models import Profile


User = get_user_model()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print("post_save")
    if kwargs.get('created'):
        print('creating')
        Cart.objects.create(user=instance)
        Profile.objects.create(user=instance)
        print('created')
