from django.db import models
 
# Create your models here.


class Surve(models.Model):
    ref_no = models.CharField(primary_key=True, max_length=50)
    house_owner = models.CharField(max_length=50)
    phone_no= models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
