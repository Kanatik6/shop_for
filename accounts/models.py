from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser,BaseUserManager



class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save()
        return user



class MyUser(AbstractUser):

    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
    
    objects = MyUserManager()



class Profile(models.Model):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    billing_address = models.CharField(max_length=100,null=True,blank=True)
    delivery_address = models.CharField(max_length=100,null=True,blank=True)
    
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name='profile')
