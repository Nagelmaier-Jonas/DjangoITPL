from django.contrib import admin
from .models import *


class StationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "ip", "roomNr"]
    pass


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["id", "command"]
    pass


class LogAdmin(admin.ModelAdmin):
    list_display = ["message", "createdAt", "get_configuration", "get_station"]

    def get_configuration(self, obj):
        return obj.station.configurationId

    def get_station(self, obj):
        return obj.station.stationId


class StationHasConfigurationJTAdmin(admin.ModelAdmin):
    pass


admin.site.register(Station, StationAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(StationHasConfigurationJT, StationHasConfigurationJTAdmin)
