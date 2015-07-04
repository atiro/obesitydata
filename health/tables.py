import django_tables2 as tables
from .models import HealthBMI, HealthActivity, HealthFruitVeg


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


class FruitVegByGenderTable(tables.Table):

    year = tables.Column(verbose_name="Year")

    fruitveg_none = tables.Column(verbose_name="No Fruit & Veg")
    fruitveg_under_1 = tables.Column(verbose_name="Less than 1 portion")
    fruitveg_under_2 = tables.Column(verbose_name="Between 1 & 2 portions")
    fruitveg_under_3 = tables.Column(verbose_name="Between 2 & 3 portions")
    fruitveg_under_4 = tables.Column(verbose_name="Between 3 & 4 portions")
    fruitveg_under_5 = tables.Column(verbose_name="Between 4 & 5 portions")
    fruitveg_more_5 = tables.Column(verbose_name="Over 5 portions")

#    female_admissions = tables.Column(verbose_name="Female")
#    unknown_admissions = tables.Column(verbose_name="Unknown")
#    total_admissions = tables.Column(verbose_name="Total")

    class Meta:
        model = HealthFruitVeg
        attrs = {"class": "paleblue"}
        exclude = ('id', 'age', 'fruitveg', 'percentage', 'gender')
