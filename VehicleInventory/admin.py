from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
	list_display = ['vehicle_model', 'vehicle_make', 'color', 'doors', 'lot_number']

admin.site.register(Vehicle, VehicleAdmin)