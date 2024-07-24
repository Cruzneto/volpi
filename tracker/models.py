from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class User(AbstractUser):
    weight = models.FloatField()

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recommended_daily_intake = models.IntegerField(default=2000)  # Valor padrão ajustável

    def __str__(self):
        return self.user.username
