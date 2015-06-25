import django_tables2 as tables
from .models import SurgeryByGender


class MaleColumn(tables.Column):
    def render(self, record):
        if record.gender == "M":
            return record.admissions


class FemaleColumn(tables.Column):
    def render(self, record):
        if record.gender == "Female":
            return record.admissions


class UnknownColumn(tables.Column):
    def render(self, record):
        if record.gender == "Unknown":
            return record.admissions


class SurgeryByGenderTable(tables.Table):

    year = tables.Column(verbose_name="Year")

# female = tables.Column(verbose_name="Female", accessor="")

    male_admissions = tables.Column(verbose_name="Male")
    female_admissions = tables.Column(verbose_name="Female")
    unknown_admissions = tables.Column(verbose_name="Unknown")

#    male = MaleColumn()
#    female = FemaleColumn()
#    unknown = UnknownColumn()

# gender = tables.Column(verbose_name="Gender")
# admissions = tables.Column(verbose_name="Admissions")

    class Meta:
        model = SurgeryByGender
        attrs = {"class": "paleblue"}
        exclude = ('id', 'code', 'gender', 'admissions')
