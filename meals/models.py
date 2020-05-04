from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class MealsCategory(models.Model):
    name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, related_name='department_id', on_delete=models.CASCADE)





