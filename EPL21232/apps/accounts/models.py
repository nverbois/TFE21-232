from django.db import models
# from django.contrib.auth.models import User # For foreign key
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from EPL21232.apps.data.models import Station

# accounts.models.py

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Adresse Email',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

#class UserStation(models.Model):
#    name = models.CharField(max_length=64, unique=True)
#    normalized_name = models.CharField(max_length=64, unique=True)
#    location = models.CharField(max_length=64)

#    def __str__(self):
#        return self.name

#    class Meta:
#        verbose_name = 'Station pluviométrique'
#        verbose_name_plural = 'Stations pluviométriques'

# Users also have a persona ( technician, system administrators, ... )
# They will be website generated, the system administrator will generate them, none of the users will be able to 
class UserRole(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Nom du rôle')
    narmalized_name = models.CharField(max_length=64, unique=True, verbose_name='Nom normalisé (ex: admin_réseau)')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rôle d\'utilisateur'
        verbose_name_plural = 'Rôles des utilisateurs'

# Create your models here.
# What should a user profile contain ?
class UserProfile(models.Model):

    # Foreign key, I want the user profile to reference a particular user
    # When we have our user reference from request.user, we can reference the profile of the user using request.user.profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil",  verbose_name='Utilisateur')
    firstname = models.CharField(max_length=64, blank=True,  verbose_name='Prénom')
    lastname = models.CharField(max_length=64, blank=True, verbose_name='Nom')

    def nom(self):
        ret = self.firstname + ' ' + self.lastname
        return ret

    # Do we need to display the full name or only the username ?
    is_full_name_displayed = models.BooleanField(default=True)

    # Details. A user posses a bio and 
    bio = models.CharField(max_length=500, blank=True, verbose_name='Description')

    # Our user profile can point at a User Persona, but they can't modify this.
    # Multiple user profile can point at the same user persona
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rôle sur la plateforme')
    stations = models.ManyToManyField(Station, blank=True, verbose_name='Stations sous gestion de l\'utilisateur')

    class Meta:
        verbose_name = 'Profil utilisateur'
        verbose_name_plural = 'Profils des utilisateurs'