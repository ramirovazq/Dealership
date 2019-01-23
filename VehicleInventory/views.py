from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets

from .models import Vehicle
from .serializers import VehicleSerializer

@login_required
def vehicles(request):
    context = {}
    context["vehicles"] = Vehicle.objects.all().order_by('-creation_date')
    return render(request, 'vehicles.html', context)    

class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vehicle.objects.all().order_by('-creation_date')
    serializer_class = VehicleSerializer
