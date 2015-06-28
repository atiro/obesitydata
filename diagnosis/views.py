from datetime import datetime
import itertools

from django.shortcuts import render_to_response, render
from django.db.models import F, Sum

from django_tables2 import RequestConfig

from diagnosis.models import AdmissionsByGender, AdmissionsByAge, SurgeryByGender

from diagnosis.tables import SurgeryByGenderTable


def admissions_by_gender(request, year=None):

    if year is not None:
        admissions = AdmissionsByGender.objects.all().filter(year=year)

        return render_to_response('diagnosis/admissions-by-gender.html',
                                  {'admissions': admissions})
    else:
        admissions = AdmissionsByGender.objects.all()

        chartdata = {
            'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in Admissions.objects.values_list('year', flat=True).distinct().order_by('year')],
            'name1': 'Male',
            'y1': AdmissionsByGender.objects.filter(gender='M').values_list('admissions', flat=True).order_by('year'),
            'name2': 'Female',
            'y2': AdmissionsByGender.objects.filter(gender='F').values_list('admissions', flat=True).order_by('year'),
            'name3': 'Unknown',
            'y3': AdmissionsByGender.objects.filter(gender='U').values_list('admissions', flat=True).order_by('year'),
        }

        charttype = 'stackedAreaChart'
        chartcontainer = 'stackedarea_container'

        table_surgery = {}
        male_admissions = admissions.values('year').annotate(male_admissions=F('admissions')).filter(gender='M')

        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': True,
                'x_axis_format': '%Y'
            }
        }

        return render_to_response('diagnosis/admissions-by-gender.html', data)

# Create your views here.


def admissions_by_age(request, year=None):

    if year is not None:
        admissions = AdmissionsByAge.objects.all().filter(year=year)

        chartdata = {
            'x': ['Under 16', '16-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75+', 'Unknown'],
            'y1': [
                admissions.values_list('age_under_16', flat=True)[0],
                admissions.values_list('age_16_to_24', flat=True)[0],
                admissions.values_list('age_25_to_34', flat=True)[0],
                admissions.values_list('age_35_to_44', flat=True)[0],
                admissions.values_list('age_45_to_54', flat=True)[0],
                admissions.values_list('age_55_to_64', flat=True)[0],
                admissions.values_list('age_65_to_74', flat=True)[0],
                admissions.values_list('age_75_and_over', flat=True)[0],
                admissions.values_list('age_unknown', flat=True)[0],
            ]
        }

        charttype = 'discreteBarChart'
#    chartcontainer = 'multibarchart_container'

        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '%s'
            }
        }

        return render_to_response('diagnosis/age-england.html', data)

    else:
        admissions = AdmissionsByAge.objects.all()

        chartdata = {
            'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in AdmissionsByAge.objects.values_list('year', flat=True).distinct().order_by('year')],
            'name1': 'Under 16',
            'y1': AdmissionsByAge.objects.all().values_list('age_under_16', flat=True).order_by('year'),
            'name2': '16-24',
            'y2': AdmissionsByAge.objects.all().values_list('age_16_to_24', flat=True).order_by('year'),
            'name3': '25-34',
            'y3': AdmissionsByAge.objects.all().values_list('age_25_to_34', flat=True).order_by('year'),
            'name4': '35-44',
            'y4': AdmissionsByAge.objects.all().values_list('age_35_to_44', flat=True).order_by('year'),
            'name5': '45-54',
            'y5': AdmissionsByAge.objects.all().values_list('age_45_to_54', flat=True).order_by('year'),
            'name6': '55-64',
            'y6': AdmissionsByAge.objects.all().values_list('age_55_to_64', flat=True).order_by('year'),
            'name7': '65-74',
            'y7': AdmissionsByAge.objects.all().values_list('age_65_to_74', flat=True).order_by('year'),
            'name8': '75+',
            'y8': AdmissionsByAge.objects.all().values_list('age_75_and_over', flat=True).order_by('year'),
            'name9': 'Unknown',
            'y9': AdmissionsByAge.objects.all().values_list('age_unknown', flat=True).order_by('year')
        }

        charttype = 'stackedAreaChart'
        chartcontainer = 'stackedarea_container'

        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': True,
                'x_axis_format': '%Y'
            }
        }

        return render_to_response('diagnosis/age-england.html', data)


def surgery_gender_england(request, year=None):

    if year is not None:
        surgery = SurgeryByGender.objects.all().filter(year=year)

        chartdata = {
            'x': ['Male', 'Female', 'Unknown'],
            'name1': 'Male',
            'y1': [
                surgery.filter(gender='M').values_list('admissions', flat=True)[0],
                surgery.filter(gender='F').values_list('admissions', flat=True)[0],
                surgery.filter(gender='U').values_list('admissions', flat=True)[0]
            ]
        }

        charttype = 'discreteBarChart'
        extra = {
            'x_is_date': False,
            'x_axis_format': '%s'
        }

    else:
        surgery = SurgeryByGender.objects.all()
        chartdata = {
            'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in surgery.values_list('year', flat=True).distinct().order_by('year')],
            'name1': 'Male',
            'y1': surgery.filter(gender='M').values_list('admissions', flat=True).order_by('year'),
            'name2': 'Female',
            'y2': surgery.filter(gender='F').values_list('admissions', flat=True).order_by('year'),
            'name3': 'Unknown',
            'y3': surgery.filter(gender='U').values_list('admissions', flat=True).order_by('year'),
            }

        charttype = 'stackedAreaChart'
        extra = {
            'x_is_date': True,
            'x_axis_format': '%Y'
        }

#    chartcontainer = 'multibarchart_container'

    table_surgery = {}
    male_surgery = surgery.values('year').annotate(male_admissions=F('admissions')).filter(gender='M')
    female_surgery = surgery.values('year').annotate(female_admissions=F('admissions')).filter(gender='F')
    unknown_surgery = surgery.values('year').annotate(unknown_admissions=F('admissions')).filter(gender='U')
    total_surgery = surgery.values('year').annotate(total_admissions=Sum('admissions'))
    for sur in itertools.chain(male_surgery, female_surgery, unknown_surgery, total_surgery):
        if sur['year'] in table_surgery:
            table_surgery[sur['year']].update(sur)
        else:
            table_surgery[sur['year']] = dict(sur)

    table = SurgeryByGenderTable(table_surgery.values())
    RequestConfig(request).configure(table)

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'extra': extra,
        'surgery_table': table
    }

    return render(request, 'diagnosis/surgery-by-gender.html', data)
