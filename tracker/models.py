from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    weight = models.FloatField()

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField()
