from django.contrib import admin

from .models import UserRole, UserProfile

# accounts.admin.py

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm, ProfileForm
from .models import User

from django.forms import SelectMultiple, CheckboxSelectMultiple
from django.db import models
#from models import *

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'active', 'staff', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class ProfileAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['nom', 'user', 'role']
    search_fields = ('firstname', 'lastname')
    form = ProfileForm
   

admin.site.register(UserProfile, ProfileAdmin)

admin.site.register(UserRole)

# Register your models here.
