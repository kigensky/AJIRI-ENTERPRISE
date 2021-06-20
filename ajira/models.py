from django.db import models
from django.contrib.auth.models import User



class EmployeeSalary(models.Model):
    id=models.AutoField(primary_key=True)
    #employee=models.ForeignKey(Employees,on_delete=models.CASCADE)
    salary_date=models.DateField()
    salary_amount=models.CharField(max_length=255)
    
    objects=models.Manager()
    
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=100)
    profile_pic= models.ImageField(upload_to='profile_pic/',)
    
    
    def __str__(self):
          return self.name

    def save_employee(self):
      self.save()

    def delete_employee(self):
      self.delete()

    @classmethod
    def find_employee(cls, employee_id):
      return cls.objects.filter(id=employee_id)

    @classmethod
    def update_employee(cls, id, name):
      update = cls.objects.filter(id=id).update(name=name)
      return update


