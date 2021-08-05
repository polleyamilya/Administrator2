from django.forms import ModelForm,Textarea
from django.db import models

# Create your models here.
class Administrator(models.Model):
    sId = models.IntegerField()
    f_name =models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email =models.EmailField(max_length=15)
class Meta:
    db_table='Administrator'    