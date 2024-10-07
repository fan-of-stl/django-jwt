from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    id = models.IntegerField(default=0, null=False, validators=[MinValueValidator(0)], primary_key=True)
    company_name = models.CharField(max_length=511, null=False, unique=True)
    company_building_name = models.CharField(max_length=255, null=False)
    company_floor = models.IntegerField(default=2, null=False, validators=[MinValueValidator(2)])
    company_parking_place_number = models.IntegerField(default=0, null=False, validators=[MinValueValidator(0)])

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  
    employee_name = models.CharField(null=False, max_length=255)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee')
    designation = models.CharField(null=False, max_length=255)
    shift = models.CharField(null=False, max_length=127)
    
    def __str__(self):
        return self.employee_name
