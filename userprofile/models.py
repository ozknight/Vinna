from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField('Contact #:', max_length=16)
    about_you = models.TextField('About You :')
    employee = models.BooleanField(default=False)
    def is_employee(self):
        return self.employee
    is_employee.boolean = True
    def __str__(self):
        return self

