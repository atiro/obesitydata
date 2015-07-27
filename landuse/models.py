from django.db import models

# Create your models here.


class LandUse(models.Model):

    gor_code = models.CharField(max_length=1)
    gor_name = models.CharField(max_length=64)
    city_code = models.IntegerField(blank=True)
    city_name = models.CharField(max_length=128)
    local_auth_code = models.CharField(max_length=4)
    local_auth_name = models.CharField(max_length=64)
    msoa_code = models.CharField(max_length=9)
    msoa_name = models.CharField(max_length=64)
    lsoa_code = models.CharField(max_length=9)
    lsoa_name = models.CharField(max_length=64)
    area_metadata = models.CharField(max_length=128, blank=True)

#   unused_field

#   Measurement in 000m^2

    total_land_area = models.FloatField()
    area_domestic_buildings = models.FloatField()
    area_non_domestic_buildings = models.FloatField()
    area_road = models.FloatField()
    area_path = models.FloatField()
    area_rail = models.FloatField()
    area_domestic_gardens = models.FloatField()
    area_greenspace = models.FloatField()
    area_water = models.FloatField()
    area_other_uses = models.FloatField()
    area_unclassified = models.FloatField()
    area_admin_geography = models.FloatField()

#   Percentage
    qof_indicator = models.FloatField()
