import django_tables2 as tables
from .models import HealthBMI


class BMIByGenderTable(tables.Table):

    year = tables.Column(verbose_name="Year")

    male_bmi = tables.Column(verbose_name="Male")
#    female_admissions = tables.Column(verbose_name="Female")
#    unknown_admissions = tables.Column(verbose_name="Unknown")
#    total_admissions = tables.Column(verbose_name="Total")

    class Meta:
        model = HealthBMI
        attrs = {"class": "paleblue"}
        exclude = ('id', 'gender', 'admissions', 'diagnosis')
