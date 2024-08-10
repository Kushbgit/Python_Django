from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    disc = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Students(models.Model):
    Name=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    Department=models.ManyToManyField(Department)   
   
    def __str__(self):
        return self.Name