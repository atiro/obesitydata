from django.db import models


class HealthWeight(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    ALL = 'A'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (ALL, 'All')
    )

    year = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    weight_mean = models.FloatField()
    weight_stderr = models.FloatField()
    base = models.IntegerField()


class HealthBMI(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    ALL = 'A'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (ALL, 'All')
    )

    AGE_16_TO_24 = '16-24'
    AGE_25_TO_34 = '25-34'
    AGE_35_TO_44 = '35-44'
    AGE_45_TO_54 = '45-54'
    AGE_55_TO_64 = '55-64'
    AGE_65_TO_74 = '65-74'
    AGE_75_PLUS = '75+'
    AGE_ALL = 'ALL'

    AGE_CHOICES = (
        (AGE_16_TO_24, '16-24'),
        (AGE_25_TO_34, '25-34'),
        (AGE_35_TO_44, '35-44'),
        (AGE_45_TO_54, '45-54'),
        (AGE_55_TO_64, '55-64'),
        (AGE_65_TO_74, '65-74'),
        (AGE_75_PLUS, '75+'),
        (AGE_ALL, 'All Ages'),
    )

    BMI_UNDERWEIGHT = 'U'
    BMI_NORMAL = 'N'
    BMI_OVERWEIGHT = 'O'
    BMI_OBESE = 'B'
    BMI_MORBIDLY_OBESE = 'M'
    BMI_OVERWEIGHT_OBESE = 'W'
    BMI_MEAN = 'E'
    BMI_STDERR = 'S'
    BMI_BASE = 'A'
    BMI_ALL = 'L'

    BMI_CHOICES = (
        (BMI_UNDERWEIGHT, 'Underweight'),
        (BMI_NORMAL, 'Normal'),
        (BMI_OVERWEIGHT, 'Overweight'),
        (BMI_OBESE, 'Obese'),
        (BMI_MORBIDLY_OBESE, 'Morbidly Obese'),
        (BMI_OVERWEIGHT_OBESE, 'Overweight including obese'),
        (BMI_MEAN, 'Mean'),
        (BMI_STDERR, 'Std error of the mean'),
        (BMI_BASE, 'Base'),
        (BMI_ALL, 'All'),
    )

    year = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    age = models.CharField(max_length=8, choices=AGE_CHOICES, default=AGE_16_TO_24)
    bmi = models.CharField(max_length=1, choices=BMI_CHOICES, default=BMI_NORMAL)

    percentage = models.FloatField(default=0.0)

# Create your models here.
