from django.contrib import admin
from .models import *


@admin.register(Station, Configuration, Log, StationHasConfigurationJT)
class StationAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name


class ConfigurationAdmin(admin.ModelAdmin):
    pass


class LogAdmin(admin.ModelAdmin):
    pass


class StationHasConfigurationJTAdmin(admin.ModelAdmin):
    pass

