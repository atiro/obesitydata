import django_tables2 as tables
from .models import SurgeryByGender, AdmissionsByAge, AdmissionsByGender


class AdmissionsByGenderTable(tables.Table):

    year = tables.Column(verbose_name="Year")

    male_admissions = tables.Column(verbose_name="Male")
    female_admissions = tables.Column(verbose_name="Female")
    unknown_admissions = tables.Column(verbose_name="Unknown")
    total_admissions = tables.Column(verbose_name="Total")

    class Meta:
        model = AdmissionsByGender
        attrs = {"class": "paleblue"}
        exclude = ('id', 'gender', 'admissions')

class AdmissionsByAgeTable(tables.Table):

    year = tables.Column(verbose_name="Year")
    age_under_16 = tables.Column(verbose_name="Under 16")
    age_16_to_24 = tables.Column(verbose_name="16-24")
    age_25_to_34 = tables.Column(verbose_name="25-34")
    age_35_to_44 = tables.Column(verbose_name="35-44")
    age_45_to_54 = tables.Column(verbose_name="45-54")
    age_55_to_64 = tables.Column(verbose_name="55-64")
    age_65_to_74 = tables.Column(verbose_name="65-74")
    age_75_and_over = tables.Column(verbose_name="75+")
    age_unknown = tables.Column(verbose_name="Unknown")
    total = tables.Column(verbose_name="Total")

    class Meta:
        model = AdmissionsByAge
        attrs = {"class": "paleblue"}
        exclude = ('id', 'gender', 'admissions')
        sequence = ('year', 'age_under_16', '...', 'age_unknown', 'total')


class SurgeryByGenderTable(tables.Table):

    year = tables.Column(verbose_name="Year")

# female = tables.Column(verbose_name="Female", accessor="")

    male_admissions = tables.Column(verbose_name="Male")
    female_admissions = tables.Column(verbose_name="Female")
    unknown_admissions = tables.Column(verbose_name="Unknown")
    total_admissions = tables.Column(verbose_name="Total")

#    male = MaleColumn()
#    female = FemaleColumn()
#    unknown = UnknownColumn()

# gender = tables.Column(verbose_name="Gender")
# admissions = tables.Column(verbose_name="Admissions")

    class Meta:
        model = SurgeryByGender
        attrs = {"class": "paleblue"}
        exclude = ('id', 'code', 'gender', 'admissions')
