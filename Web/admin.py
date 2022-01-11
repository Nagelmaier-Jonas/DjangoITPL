from django.contrib import admin
from .models import *


class StationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "url", "roomNr"]
    search_fields = ["name"]


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["id", "command", 'delay']
    search_fields = ["command"]


class LogAdmin(admin.ModelAdmin):
    list_display = ["station", "message", "createdAt", "configuration"]
    list_filter = ["createdAt"]

    def configuration(self, obj):
        return obj.station_jt.configurationId

    def station(self, obj):
        return obj.station_jt.stationId


class StationHasConfigurationJTAdmin(admin.ModelAdmin):
    list_display = ["stationId", "configurationId"]
    list_filter = ["stationId__name"]


admin.site.register(Station, StationAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(StationHasConfigurationJT, StationHasConfigurationJTAdmin)
