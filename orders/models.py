from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=50)

class Status(models.Model):
    name = models.CharField(max_length=50)

class ServicePercentage(models.Model):
    percentage = models.IntegerField()
