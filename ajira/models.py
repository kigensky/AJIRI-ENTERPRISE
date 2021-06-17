from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

departments=[('Human Resource','Human Resource'),
('Marketing','Marketing'),
('Accounting','Accounting'),

]

class Employees(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=20, choices=departments,default='Marketing')
    address = models.TextField(max_length=50)
    status = models.CharField(max_length=20)
    job_title = models.CharField(max_length=50)
    
    
    def __str__(self):
      return self.name

    def save_employee(self):
      self.save()

    def delete_employee(self):
       self.delete()

    @classmethod
    def find_employee(cls, hood_id):
      return cls.objects.filter(id=EmployeeList)
      return cls.objects.filter(id=employee_id)

    @classmethod
    def update_neighborhood(cls, id, name):
      update = cls.objects.filter(id=id).update(name=name)
      return update




