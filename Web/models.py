import datetime

from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=25, unique=True)
    ip = models.CharField(max_length=25, unique=True)
    roomNr = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Configuration(models.Model):
    command = models.CharField(max_length=200)

    def __str__(self):
        return self.command


class StationHasConfigurationJT(models.Model):
    id = models.AutoField(primary_key = True)
    stationId = models.ForeignKey(Station, on_delete=models.CASCADE)
    configurationId = models.ForeignKey(Configuration, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Log(models.Model):
    message = models.TextField()
    createdAt = models.DateTimeField()
    station = models.ForeignKey(StationHasConfigurationJT, on_delete=models.CASCADE)

    def __str__(self):
        return self.createdAt.strftime("%d.%m.%y %H:%M")
