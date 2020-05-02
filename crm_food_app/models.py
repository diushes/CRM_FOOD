from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=50)

class Role(models.Model):
    name = models.CharField(max_length=50)

class Department(models.Model):
    name = models.CharField(max_length=50)


