from django.db import models

# Create your models here.
class route(models.Model):
    name = models.CharField(max_length=30)
    name = models.IntegerField(max_length=20)
    coordinates = models.CharField()