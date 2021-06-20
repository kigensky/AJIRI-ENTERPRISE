from django.db import models
from django.contrib.auth.models import User

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
    def find_employee(cls, employee_id):
      return cls.objects.filter(id=employee_id)

    @classmethod
    def update_employee(cls, id, name):
      update = cls.objects.filter(id=id).update(name=name)
      return update



class Leave(models.Model):
    Employeename = models.CharField(max_length=50)
    department = models.CharField(max_length=20, choices=departments,default='Marketing')
    m = (
        ("January","January"),("February","February"),("March","March"),("April","April"),("May","May"),("June","June"),("July","July"),("August","August"),("September","September"),("October","October"),("November","November"),("December","december")
    )
    month = models.CharField(max_length=10, choices= m)
    year = models.IntegerField()
    Start_Date = models.DateField()
    End_Date = models.DateField(null=True, blank = True)
    Reason = models.CharField(max_length=200)


    def __str__(self):
        return str(self.Employee_Name)

        
    def save_leave(self):
      self.save()


    def delete_leave(self):
      self.delete() 

    
    @classmethod
    def find_employee(cls,name):
        return cls.objects.filter(name__icontains=name)

          
    @classmethod
    def get_employee(cls,name):
        employee = cls.objects.filter(employee__name__icontains=name)
        return employee   
    
    @property
    def get_name(self):
        return self.name
      
    @property
    def get_id(self):
        return self.user.id
      
  

