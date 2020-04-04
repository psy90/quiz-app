from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from rest_framework.authtoken.models import Token


class TimeStamp(models.Model):
    """
    Model contains created and updated date time fields.
    These fields can be abstract in other models
    """

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """
    Manager to override the user creation with email
    """

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not email:
            raise ValueError('User must have email')
        if not password:
            raise ValueError('User must have password')

        user_obj = self.model(email=email, **extra_fields)
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser, TimeStamp):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(pre_save, sender=User)
def change_username(sender, instance=None, created=False, **kwargs):
    if instance and created is False:
        instance.username = instance.email
        return instance
