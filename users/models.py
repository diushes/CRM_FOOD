from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):

    def _create_user(self, login, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not login:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(login=login, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, login, password=None, **extra_fields):
        #extra_fields.setdefault('is_staff', False)
        #extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        #extra_fields.setdefault('is_staff', True)
        #extra_fields.setdefault('is_superuser', True)

        return self._create_user(login, password=password, **extra_fields)

class Role(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    """
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    roleid = models.ForeignKey(Role, related_name='roleid',on_delete=models.CASCADE)
    dateofadd = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name', 'surname', 'email', 'roleid', 'phone']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


#class User(models.Model):
#    name = models.CharField(max_length=50)
#    surname = models.CharField(max_length=50)
#    email = models.CharField(max_length=50)
#    roleid = models.ForeignKey(Role, related_name='roleid',on_delete=models.CASCADE)
#    dateofadd = models.DateTimeField(auto_now_add=True)
#    phone = models.CharField(max_length=50)
#    login = models.CharField(max_length=50)
#    password = models.CharField(max_length=50)
#