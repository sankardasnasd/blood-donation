from django.db import models

# Create your models here.

class login_table(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    type =  models.CharField(max_length=10)
class blood_table(models.Model):
   bloodgroup = models.CharField(max_length=100)
   date = models.CharField(max_length=100)
   details = models.CharField(max_length=100)
class user_table(models.Model):
   firstname =  models.CharField(max_length=100)
   lastname = models.CharField(max_length=100)
   age = models.IntegerField()
   gender = models.CharField(max_length=100)
   place = models.CharField(max_length=100)
   post = models.CharField(max_length=100)
   pin = models.IntegerField()
   phonno = models.BigIntegerField()
   email = models.CharField(max_length=100)
   BLOOD = models.ForeignKey(blood_table,on_delete=models.CASCADE)
   LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
class hospital_table(models.Model):
   name = models.CharField(max_length=100)
   place = models.CharField(max_length=100)
   post = models.CharField(max_length=100)
   pin = models.IntegerField()
   city =models.CharField(max_length=100)
   state = models.CharField(max_length=100)
   phonno = models.BigIntegerField()
   email = models.CharField(max_length=100)
   LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)

class feedback_table(models.Model):
    feedback= models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    USER =models.ForeignKey(user_table, on_delete=models.CASCADE)
    HOSPITAL= models.ForeignKey(hospital_table, on_delete=models.CASCADE)

class complaint_table(models.Model):
    complaint = models.CharField(max_length=300)
    replay = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    HOSPITAL = models.ForeignKey(hospital_table, on_delete=models.CASCADE)

class request_table(models.Model):
    blood =  models.ForeignKey(blood_table, on_delete=models.CASCADE)
    details = models.CharField(max_length=300)
    date=models.DateField()
    count = models.IntegerField()
    status = models.CharField(max_length=300)
    HOSPITAL = models.ForeignKey(hospital_table, on_delete=models.CASCADE)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)

class response_table(models.Model):
    REQUEST =  models.ForeignKey(request_table, on_delete=models.CASCADE)
    date=models.DateField()
    status = models.CharField(max_length=300)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)

class blood_bank_table(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    phonno =models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    HOSPITAL = models.ForeignKey(hospital_table, on_delete=models.CASCADE)
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)


class Stock(models.Model):
    BLOOD =  models.ForeignKey(blood_table, on_delete=models.CASCADE)
    BANK =  models.ForeignKey(blood_bank_table, on_delete=models.CASCADE)
    stock = models.CharField(max_length=300)

    