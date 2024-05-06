from django.db import models
from django.urls import reverse

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('location-detail', args=[str(self.id)])

class Route(models.Model):
    name = models.CharField(max_length=30)
    start = models.ForeignKey(Location, on_delete=models.RESTRICT, related_name="start")
    destination = models.ForeignKey(Location, on_delete=models.RESTRICT, related_name="destination")

