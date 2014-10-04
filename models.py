from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=45)
    tagline=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='logos',blank=True)
    description=models.TextField()

    def __str__(self):
        return self.name
 
   
class Employee(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    company=models.ManyToManyField(Company)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Customer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15)
    comment=models.TextField()
    company=models.ForeignKey(Company)

    def __str__(self):
        return 'Customer: {0} {1}'.format(self.first_name, self.last_name)


