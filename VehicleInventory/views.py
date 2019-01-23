from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Vehicle

@login_required
def vehicles(request):
    context = {}
    context["vehicles"] = Vehicle.objects.all()
    return render(request, 'vehicles.html', context)    
