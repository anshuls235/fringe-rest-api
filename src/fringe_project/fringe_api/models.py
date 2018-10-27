from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django work with the custom User Model."""

    def create_user(self, email, corporate_email, name, password=None):
        """Create a new user profile object."""

        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)

        user = self.model(
                email=email,
                corporate_email=corporate_email,
                name=name
            )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, corporate_email, name, password):
        """Creates and saves a new superuser with the given details."""

        user = self.create_user(email,corporate_email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents the User Profile inside our system."""

    corporate_email = models.EmailField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['corporate_email','name']

    def get_full_name(self):
        """Used to get users full name."""

        return self.name

    def get_short_name(self):
        """Used to get users short name."""

        return self.name

    def __str__(self):
        """Coverts the object to string."""

        return self.email
