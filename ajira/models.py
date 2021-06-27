from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models



# Create your models here.
departments=[('Human Resource','Human Resource'),
('Marketing','Marketing'),
('Accounting','Accounting'),
]
class UserCustomManager(UserManager):
  def create_superuser(self, email=None, password=None, **kwargs):
    if not email:
      raise TypeError("superusers must have an email")
    if not password:
      raise TypeError("superuser must have a password")
    user = self.model(email=email)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.set_password(password)   
    user.save()
    
    


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserCustomManager()



class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    department = models.CharField(max_length=20, choices=departments,default='Marketing')
    address = models.TextField(max_length=50)
    status = models.CharField(max_length=20)
    job_title = models.CharField(max_length=50)
    def __str__(self):
      return self.employee_name
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
class EmployeeSalary(models.Model):
    id=models.AutoField(primary_key=True)
    employee_name=models.ForeignKey(Employee,on_delete=models.CASCADE)
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
class Leave(models.Model):
    employee_name=models.ForeignKey(Employee,on_delete=models.CASCADE)
    # department = models.CharField(max_length=20, choices=departments,default='Marketing')
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
