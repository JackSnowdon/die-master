from django.db import models
from accounts.models import Profile

# Create your models here.


class DarkHeresyGame(models.Model):
    name = models.CharField(max_length=255)
    dm = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name