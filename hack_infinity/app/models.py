from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.models import model_to_dict
# Create your models here.


class MyUser(AbstractUser):
    mobile_no = models.CharField(max_length=10, unique=True)
    user_type = models.NullBooleanField(null=True)


class State_translator(models.Model):
    state_name = models.CharField(max_length=50, default=None)
    state_language = models.CharField(max_length=50, default=None)
    state_code = models.CharField(max_length=20, default="en")

    def __str__(self):
        return self.state_name

    def to_dict(self):
        return model_to_dict(self)


class Produce(models.Model):
    user = models.ForeignKey('MyUser')
    crop = models.CharField(max_length=30)
    quantity = models.IntegerField()
