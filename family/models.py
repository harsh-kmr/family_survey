from django.db import models

# Create your models here.

class Parents(models.Model):
     Husband_Name = models.CharField(max_length= 100)
     Wife_name = models.CharField(max_length= 100)


class Childrens(models.Model):
    parent_id = models.ForeignKey(Parents, on_delete= models.CASCADE)
    Child_Name = models.CharField(max_length=100)