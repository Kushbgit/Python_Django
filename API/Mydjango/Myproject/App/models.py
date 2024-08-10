from django.db import models

# Create your models here.
class Students(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    def __str__(self):
        return self.Name+' '+self.Email
    #For Generating Query -> py manage.py makemigrations -> ORM is reponsible for generating = OBJECT RELATIONAL METHOD
    class Meta:
        db_table='Students'
        verbose_name_plural = 'Students'
        # verbose_name = 'Student'
        ordering=['Name']