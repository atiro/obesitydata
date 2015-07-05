from django.db import models

# Create your models here.


class CodePoint(models.Model):

    postcode = models.CharField(max_length=7)
    pos_quality = models.IntegerField()
    eastings = models.IntegerField()
    northings = models.IntegerField()
    country_code = models.CharField(max_length=9)
    nhs_regional_ha_code = models.CharField(max_length=9)
    nhs_ha_code = models.CharField(max_length=9)
    admin_county_code = models.CharField(max_length=9)
    admin_district_code = models.CharField(max_length=9)
    admin_ward_code = models.CharField(max_length=9)
