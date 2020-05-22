from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile
from game.models import DarkHeresyGame, DarkDieRoll

# Create your models here.

class DarkHeresyBase(models.Model):
    name = models.CharField(max_length=255)
    weapon_skill = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    ballistic_skill = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    strengh = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    toughness = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    agility = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    intelligence = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    perception = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    willpower = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    fellowship = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    influence = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    max_fate_points = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    created_by = models.ForeignKey(Profile, related_name='dh_sheets', on_delete=models.PROTECT)
    current_game = models.ForeignKey(DarkHeresyGame, related_name='sheets', on_delete=models.PROTECT, blank=True,
        null=True)
    die_roll = models.ForeignKey(DarkDieRoll, related_name='die_rolls', on_delete=models.PROTECT, blank=True,
        null=True)

    def __str__(self):
        return self.name