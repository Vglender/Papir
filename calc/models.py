from django.db import models

# class Department(models.Model):
#     department_title = models.CharField(max_length=30)
#     department_location = models.CharField(max_length=100)
#     department_description = models.CharField(max_length=100)

class Unit(models.Model):
    unit_title = models.CharField(max_length=10)
    unit_description = models.CharField(max_length=30)

# class Eployees(models.Model):
#     firstName = models.CharField(max_length=10)
#     lastName = models.CharField(max_length=20)
#     # department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
#
# class Operation(models.Model):
#     type_operation = models.CharField(max_length=100)
#     unit_type = models.ForeignKey(Unit, null=True, blank=True,  on_delete=models.CASCADE)
#     unit_cost = models.FloatField()
#     employee = models.ForeignKey(Eployees, null=True, blank=True, on_delete=models.CASCADE)












# Create your models here.
