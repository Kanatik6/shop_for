from django.contrib import admin

from accounts.models import Profile
from accounts.models import MyUser

admin.site.register(MyUser)
admin.site.register(Profile)
