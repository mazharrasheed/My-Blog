from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blog(models.Model):

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.RESTRICT,default=2)

