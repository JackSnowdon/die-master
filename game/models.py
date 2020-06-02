from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile

# Create your models here.


class DarkHeresyGame(models.Model):
    name = models.CharField(max_length=255)
    dm = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ready_state = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DarkDieRoll(models.Model):
    target_id = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], default=0)
    roll_type = models.CharField(max_length=255)
    roll_amount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    roll_game = models.ForeignKey(DarkHeresyGame, related_name='all_game_rolls', on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)
    fate_points = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def __str__(self):
        return "{0} Die Roll For Id: {1}".format(self.roll_type, self.target_id)
