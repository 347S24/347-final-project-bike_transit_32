from django.db import models
from users.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Route(models.Model):
    name = models.CharField(max_length=30)
    start = models.ForeignKey(Location)
    destination = models.ForeignKey(Location)
    creator = models.ForeignKey(User)

