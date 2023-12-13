from django.db import models
# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=50)
    hiring_date = models.DateField()
    
    
    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)