from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile

# Create your models here.


class DarkHeresyGame(models.Model):
    name = models.CharField(max_length=255)
    dm = models.OneToOneField(Profile, on_delete=models.CASCADE)
    ready_state = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DarkDieRoll(models.Model):
    target_id = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], default=0)
    roll_type = models.CharField(max_length=255)
    roll_amount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    passed = models.BooleanField(default=False)
