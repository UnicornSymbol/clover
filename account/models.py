from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Profile(models.Model):
    '''User's Profile'''
    user = models.ForeignKey(User,unique=True,verbose_name=_('user'))
