from django.db import models
from django.contrib.auth.models import User # For foreign key

class UserStation(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    location = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# Users also have a persona ( technician, system administrators, ... )
# They will be website generated, the system administrator will generate them, none of the users will be able to 
class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    narmalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
# What should a user profile contain ?
class UserProfile(models.Model):

    # Foreign key, I want the user profile to reference a particular user
    # When we have our user reference from request.user, we can reference the profile of the user using request.user.profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil")

    # Do we need to display the full name or only the username ?
    is_full_name_displayed = models.BooleanField(default=True)

    # Details. A user posses a bio and 
    bio = models.CharField(max_length=500, blank=True, null=True)

    # Our user profile can point at a User Persona, but they can't modify this.
    # Multiple user profile can point at the same user persona
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)
    stations = models.ManyToManyField(UserStation, blank=True)
