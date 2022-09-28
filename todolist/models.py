from datetime import datetime
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    title = models.CharField(max_length=250)
    description = models.TextField()
    finished = models.BooleanField(default=False)