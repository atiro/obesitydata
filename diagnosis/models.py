from django.db import models

# Create your models here.

MALE = 'M'
FEMALE = 'F'
UNKNOWN = 'U'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (UNKNOWN, 'Unknown'))


class Admissions(models.Model):
    year = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    admissions = models.IntegerField()


class AdmissionsByAge(models.Model):

    year = models.IntegerField()

    total = models.IntegerField()

    age_under_16 = models.IntegerField()
    age_16_to_24 = models.IntegerField()
    age_25_to_34 = models.IntegerField()
    age_35_to_44 = models.IntegerField()
    age_45_to_54 = models.IntegerField()
    age_55_to_64 = models.IntegerField()
    age_65_to_74 = models.IntegerField()
    age_75_and_over = models.IntegerField()
    age_unknown = models.IntegerField()


class SurgeryByGender(models.Model):

    code = models.FloatField()

    year = models.IntegerField()

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    admissions = models.IntegerField()
