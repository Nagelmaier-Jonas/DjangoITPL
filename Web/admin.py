from django.contrib import admin
from .models import *


class StationAdmin(admin.ModelAdmin):
    pass


class ConfigurationAdmin(admin.ModelAdmin):
    pass


class LogAdmin(admin.ModelAdmin):
    list_display = ["message", "createdAt", "station_configurationId"]
    pass


class StationHasConfigurationJTAdmin(admin.ModelAdmin):
    pass


admin.site.register(Station, StationAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(StationHasConfigurationJT, StationHasConfigurationJTAdmin)
