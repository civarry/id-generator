from django.db import models
from dateutil.relativedelta import relativedelta
import datetime

expiration = datetime.datetime.now() + relativedelta(years=5)

class UserInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    CIVIL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Live-in', 'Live-in'),
        ('Separated', 'Separated'),
        ('Widow/er', 'Widow/er'),
    )
    civil_status = models.CharField(max_length=255, choices=CIVIL_STATUS, null=True, blank=True)

    BLOOD_TYPE = (
        ('A+','A+'),
        ('O+','O+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('O-','O-'),
        ('B-','B-'),
        ('AB-','AB-'),
    )
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE, null=True, blank=True)
    date_issued = models.DateField(auto_now_add=True)
    validity = models.DateField(default = expiration)
    motto = models.TextField()

    def __str__(self):
        return self.first_name
