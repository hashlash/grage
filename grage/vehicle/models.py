from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='components')

    def __str__(self):
        return self.name
