from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar_no = models.IntegerField(unique=True)  
    created_date = models.DateTimeField() 
    created_by = models.CharField(max_length=50) 

    def __str__(self):
        return str(self.aadhar_no)
        
class Students(models.Model):
    Name=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.PROTECT)