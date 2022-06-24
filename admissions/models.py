from django.db import models

from django.urls import reverse
from datetime import datetime

# Create your models here.

    


class Students_info(models.Model):       # irrespective of casing you use, inside database it will be saved as lowercase(Student --> student)
    Roll_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)           # It is similar to VarChar in Mysql
    father_name = models.CharField(max_length = 100)
    class_name = models.IntegerField()
    contact = models.CharField(max_length = 15)  # since mobile number also include + , spaces and numbers
    amount_fee_paid = models.IntegerField(default=1000000)
    date_of_admission = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField()
    
