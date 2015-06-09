from django.db import models

# Create your models here.
class Admissions(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'
    GENDER_CHOICES = (
            (MALE, 'Male'), 
            (FEMALE, 'Female'), 
            (UNKNOWN, 'Unknown'))

    year = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    admissions = models.IntegerField()
