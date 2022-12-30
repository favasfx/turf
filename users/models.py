from django.db import models

# Create your models here.

class Users(models.Model):
      
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)
    


    class Meta:
        db_table = 'users'


class Bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    class Meta:
        db_table = 'bookings'


class Feedbacks(models.Model):
    feedback = models.CharField(max_length=100) 

    class Meta:
        db_table = 'feedbacks'  

class Testclass(models.Model):
    testfield = models.CharField(max_length=100)

    class Meta:
        db_table = 'testtable'     

 







