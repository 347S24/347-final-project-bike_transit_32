from django.shortcuts import render
from .models import Route, Location
# Create your views here.

def index(request):
    """View function for home page of site."""
    context = {
        'num_routes': 0,
    }

    return render(request, 'index.html', context=context)

def login(request):
    """View function for home page of site."""

    context = {
        'num_routes': 0,
    }

    return render(request, 'login.html', context)

def logout(request):
    return render(request, 'logged_out.hmtl')

def routes(request):
    """View function for home page of site."""

    context = {
        'num_routes': 0,
    }

    return render(request, 'route_finder.html', context)

def saved_routes(request):
    routes = Route.objects.all().values()
    locations = Location.objects.values()
    context = {
        'num_routes': 0,
        'routes': routes,
        'locations': locations,
    }
    return render(request, 'saved_routes.html', context)