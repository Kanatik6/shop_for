from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.cart.models import Cart
from accounts.models import Profile


User = get_user_model()

@receiver(post_save, sender=User)
def save_profile(sender, instance, created,**kwargs):
    print("post_save")
    if created:
        print('creating')
        Cart.objects.get_or_create(user=instance)
        Profile.objects.get_or_create(user=instance)
        print('created')
