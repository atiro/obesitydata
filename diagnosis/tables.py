import django_tables2 as tables
from .models import SurgeryByGender, AdmissionsByAge


class AdmissionsByAgeTable(tables.Table):

    year = tables.Column(verbose_name="Year")
    admissions_under_16 = tables.Column(verbose_name="Under 16")

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
