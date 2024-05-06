from django.contrib import admin
from .models import Route, Location

# Register your models here.
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'destination')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')