from django.contrib import admin

from grage.vehicle.models import Component, Vehicle

admin.site.register([
    Vehicle, Component,
])
