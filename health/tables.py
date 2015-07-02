import django_tables2 as tables
from .models import HealthBMI, HealthActivity


class BMIByGenderTable(tables.Table):

    year = tables.Column(verbose_name="Year")

    underweight_bmi = tables.Column(verbose_name="Underweight")
    normal_bmi = tables.Column(verbose_name="Normal")
    overweight_bmi = tables.Column(verbose_name="Overweight")
    obese_bmi = tables.Column(verbose_name="Obese")
    morbidly_bmi = tables.Column(verbose_name="Morbidly Obese")

#    female_admissions = tables.Column(verbose_name="Female")
#    unknown_admissions = tables.Column(verbose_name="Unknown")
#    total_admissions = tables.Column(verbose_name="Total")

    class Meta:
        model = HealthBMI
        attrs = {"class": "paleblue"}
        exclude = ('id', 'age', 'bmi', 'percentage', 'gender')


class ActivityByGenderTable(tables.Table):

    year = tables.Column(verbose_name="Year")

    activity_meets = tables.Column(verbose_name="Meets Activity")
    activity_some = tables.Column(verbose_name="Some Activity")
    activity_low = tables.Column(verbose_name="Low Activity")

#    female_admissions = tables.Column(verbose_name="Female")
#    unknown_admissions = tables.Column(verbose_name="Unknown")
#    total_admissions = tables.Column(verbose_name="Total")

    class Meta:
        model = HealthActivity
        attrs = {"class": "paleblue"}
        exclude = ('id', 'age', 'activity', 'percentage', 'gender')
