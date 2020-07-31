from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from useraccount.models import Profile, Addfriend, Review
# Register your models here.

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Profile)
admin.site.register(Addfriend)
admin.site.register(Review)
