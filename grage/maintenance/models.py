from django.db import models

from grage.vehicle.models import Component, Vehicle


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenances')
    # TODO: consider using JSONField for storing current conditions
    odometer = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vehicle} maintenance at {self.timestamp}'


class MaintenanceItem(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    # TODO: verify vehicle
    component = models.ForeignKey(Component, on_delete=models.RESTRICT, related_name='maintenances')

    def __str__(self):
        return f'{self.component}: {self.name}'
