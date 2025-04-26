from django.db import models
from datetime import date
# Create your models here.
class Enquries(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    subject= models.CharField(max_length=50)
    msg= models.TextField()
    date = models.DateField(default=date.today)

    # def __str__(self):
    #     return f'{self.name,self.email,self.phone,self.subject,self.msg}'