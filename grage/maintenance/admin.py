from django.contrib import admin

from grage.maintenance.models import Maintenance, MaintenanceItem

admin.site.register([
    Maintenance, MaintenanceItem,
])
