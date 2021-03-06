from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class MealsCategory(models.Model):
    name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, related_name='department_id', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Meal(models.Model):
    field = models.Field(primary_key=True)
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(MealsCategory, related_name='categoryid', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(max_length=150, default='')


