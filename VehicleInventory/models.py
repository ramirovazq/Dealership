from django.db import models

# Create your models here.
class Vehicle(models.Model):

    vehicle_make = models.CharField(
            blank=False,
            null = True,
            max_length=300
    )

    vehicle_model = models.CharField(
            blank=False,
            null = True,
            max_length=300
    )

    description = models.TextField(
            blank=True,
            null = True,
    )

    color = models.CharField(
            blank=False,
            null = True,
            max_length=300
    )

    doors = models.PositiveSmallIntegerField(
            blank=False,
            null = False,
            default=2
    )

    lot_number = models.CharField(
            blank=False,
            null = True,
            max_length=300
    )


    def __str__(self):
        return "{} {}, color {}, doors {}".format(self.vehicle_make, self.vehicle_model, self.color, self.doors)
