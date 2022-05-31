from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class user_details(models.Model):
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=150,null=True)
    address = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    mobilenumber = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)

class mechanics_details(models.Model):
    name = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    mobilenumber = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    category = models.CharField(max_length=150,null=True)
    assign_payment = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

class descriptions(models.Model):
    username = models.CharField(max_length=150,blank=True)
    place = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)

class notifications(models.Model):
    user_id = models.CharField(max_length=150)
    msg = models.CharField(max_length=150)
class admin_reply(models.Model):

    msg = models.CharField(max_length=150)
class status(models.Model):
    mechanic_name = models.CharField(max_length=150)
    customer_name = models.CharField(max_length=150)
    customer_mobile = models.CharField(max_length=150)
    location = models.CharField(max_length=150, null=True)
    payment_status = models.CharField(max_length=150, null=True)
    #otp = models.CharField(max_length=150, null=True)


class admin_table(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class feedbacks(models.Model):
    feedback = models.CharField(max_length=100)


    def __str__(self):
        return self.name
