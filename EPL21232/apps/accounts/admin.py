from django.contrib import admin

from .models import UserPersona, UserProfile, UserStation

admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(UserStation)

# Register your models here.
