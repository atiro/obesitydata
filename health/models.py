from django.db import models


class HealthActivity(models.Model):
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

    ACTIVITY_MEETS = 'Meets'
    ACTIVITY_SOME = 'Some'
    ACTIVITY_LOW = 'Low'
    ACTIVITY_BASES = 'Bases'

    ACTIVITY_CHOICES = (
        (ACTIVITY_MEETS, 'Meets Activity'),
        (ACTIVITY_SOME, 'Some Activity'),
        (ACTIVITY_LOW, 'Low Activity'),
        (ACTIVITY_BASES, 'Bases'),
    )

    year = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    age = models.CharField(max_length=8, choices=AGE_CHOICES, default=AGE_16_TO_24)
    activity = models.CharField(max_length=5, choices=ACTIVITY_CHOICES, default=ACTIVITY_MEETS)

    percentage = models.FloatField(default=0.0)


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


class HealthFruitVeg(models.Model):
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

    FRUITVEG_NONE = 'N'
    FRUITVEG_LESS_1 = '1'
    FRUITVEG_LESS_2 = '2'
    FRUITVEG_LESS_3 = '3'
    FRUITVEG_LESS_4 = '4'
    FRUITVEG_LESS_5 = '5'
    FRUITVEG_MORE_5 = '6'
    FRUITVEG_MEAN = 'M'
    FRUITVEG_STDERR = 'S'
    FRUITVEG_MEDIAN = 'D'
    FRUITVEG_BASE = 'B'

    FRUITVEG_CHOICES = (
        (FRUITVEG_NONE, 'No Fruit & Veg'),
        (FRUITVEG_LESS_1, 'Under 1 portion'),
        (FRUITVEG_LESS_2, '1-2 Portions'),
        (FRUITVEG_LESS_3, '2-3 Portions'),
        (FRUITVEG_LESS_4, '3-4 Portions'),
        (FRUITVEG_LESS_5, '4-5 Portions'),
        (FRUITVEG_MORE_5, '5+ Portions'),
        (FRUITVEG_MEAN, 'Mean Portions'),
        (FRUITVEG_STDERR, 'Standard error of the mean'),
        (FRUITVEG_MEDIAN, 'Median Portions'),
        (FRUITVEG_BASE, 'Standard error of the mean')
    )

    year = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    age = models.CharField(max_length=8, choices=AGE_CHOICES, default=AGE_16_TO_24)
    fruitveg = models.CharField(max_length=1, choices=FRUITVEG_CHOICES, default=FRUITVEG_NONE)

    percentage = models.FloatField(default=0.0)

# Create your models here.
