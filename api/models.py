from django.db import models

# Create your company models here.



class company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=500,choices=(
        ('IT','IT'),
        ('NON IT','NON IT'),
    ))
    add_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self) :
        return self.name



class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    about=models.TextField()
    phone=models.TextField()
    postion=models.CharField(max_length=500,choices=(
        ('dev','dev'),
        ('NON IT','NON IT'),))
    
    

    company=models.ForeignKey(company, on_delete=models.CASCADE)