from datetime import datetime
import itertools
import json

from django.shortcuts import render
from django.db.models import F, Sum
from django.http import JsonResponse, HttpResponse

from django_tables2 import RequestConfig

from diagnosis.models import AdmissionsByGender, AdmissionsByAge, SurgeryByGender 

from diagnosis.tables import SurgeryByGenderTable, AdmissionsByAgeTable, AdmissionsByGenderTable


def admissions_by_gender(request, year=None, gender=None, diagnosis=AdmissionsByGender.PRIMARY):

    if year is not None:
        admissions = AdmissionsByGender.objects.all().filter(year=year).filter(diagnosis=diagnosis)
    else:
        admissions = AdmissionsByGender.objects.all().filter(diagnosis=diagnosis)

    if gender is not None:
        admissions = admissions.filter(gender=gender)

    if 'application/json' in request.META.get('HTTP_ACCEPT'):
        chartdata = {
            'x': list([int(datetime(x, 1, 1).strftime('%s'))*1000 for x in admissions.values_list('year', flat=True).distinct().order_by('year')]),
            'gender': gender,
            'y1': list(admissions.values_list('admissions', flat=True).order_by('year')),

        }
        summary = "In 2013-2014, %s  %s patients received a primary diagnosis of obesity." % ( chartdata["y1"][-1], 'Male' if gender == 'M' else 'Female'),

        return JsonResponse([{'key': chartdata['gender'], 'values': zip(chartdata['x'], chartdata['y1']), 'summary': summary}], safe=False)

    chartdata = {
        'x': list([int(datetime(x, 1, 1).strftime('%s'))*1000 for x in admissions.values_list('year', flat=True).distinct().order_by('year')]),
        'name1': 'Male',
        'y1': list(admissions.filter(gender='M').values_list('admissions', flat=True).order_by('year')),
        'name2': 'Female',
        'y2': list(admissions.filter(gender='F').values_list('admissions', flat=True).order_by('year'))
    }

    if diagnosis == AdmissionsByGender.PRIMARY:
        chartdata['name3'] = 'Unknown'
        chartdata['y3'] = list(admissions.filter(gender='U').values_list('admissions', flat=True).order_by('year'))

    charttype = 'stackedAreaChart'
    chartcontainer = 'stackedarea_container'

    table_admissions = {}
    male_admissions = admissions.values('year').annotate(male_admissions=F('admissions')).filter(gender='M')
    female_admissions = admissions.values('year').annotate(female_admissions=F('admissions')).filter(gender='F')
    unknown_admissions = admissions.values('year').annotate(unknown_admissions=F('admissions')).filter(gender='U')
    total_admissions = admissions.values('year').annotate(total_admissions=Sum('admissions'))

    for sur in itertools.chain(male_admissions, female_admissions, unknown_admissions, total_admissions):
        if sur['year'] in table_admissions:
            table_admissions[sur['year']].update(sur)
        else:
            table_admissions[sur['year']] = dict(sur)

    table = AdmissionsByGenderTable(table_admissions.values())
    RequestConfig(request).configure(table)

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'surgery_table': table,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%Y',
            'y_axis_format': '%.0d'
        }
    }

    return render(request, 'diagnosis/admissions-by-gender.html', data)

# Create your views here.


def admissions_by_age(request, year=None, gender=None, age=None, diagnosis=AdmissionsByAge.PRIMARY):

    admissions = AdmissionsByAge.objects.all().filter(diagnosis=diagnosis)

    if year is not None:
        admissions = admissions.objects.filter(year=year)

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
        extra = {
            'x_is_date': False,
            'x_axis_format': '%s'
        }

    else:

        if 'application/json' in request.META.get('HTTP_ACCEPT'):
            chartdata = {
                'x': list([int(datetime(x, 1, 1).strftime('%s'))*1000 for x in admissions.values_list('year', flat=True).distinct().order_by('year')]),
                }

            chartdata['age'] = age
            if age == "0-16":
                chartdata['y'] = list(admissions.values_list('age_under_16', flat=True).order_by('year'))
            elif age == "16-24":
                chartdata['y'] = list(admissions.values_list('age_16_to_24', flat=True).order_by('year'))
            elif age == "25-34":
                chartdata['y'] = list(admissions.values_list('age_25_to_34', flat=True).order_by('year'))
            elif age == "35-44":
                chartdata['y'] = list(admissions.values_list('age_35_to_44', flat=True).order_by('year'))
            elif age == "45-54":
                chartdata['y'] = list(admissions.values_list('age_45_to_54', flat=True).order_by('year'))
            elif age == "55-64":
                chartdata['y'] = list(admissions.values_list('age_55_to_64', flat=True).order_by('year'))
            elif age == "65-74":
                chartdata['y'] = list(admissions.values_list('age_65_to_74', flat=True).order_by('year'))
            elif age == "75+":
                chartdata['y'] = list(admissions.values_list('age_75_and_over', flat=True).order_by('year'))

            summary = "In 2013-2014, %s diagnosis of obesity were given to those aged %s." % (chartdata['y'][-1], age)

            return JsonResponse([{'key': chartdata['age'], 'values': zip(chartdata['x'], chartdata['y']), 'summary': summary}], safe=False)

        chartdata = {
            'x': list([int(datetime(x, 1, 1).strftime('%s'))*1000 for x in admissions.values_list('year', flat=True).distinct().order_by('year')]),
            'name1': 'Under 16',
            'y1': list(admissions.all().values_list('age_under_16', flat=True).order_by('year')),
            'name2': '16-24',
            'y2': list(admissions.all().values_list('age_16_to_24', flat=True).order_by('year')),
            'name3': '25-34',
            'y3': list(admissions.all().values_list('age_25_to_34', flat=True).order_by('year')),
            'name4': '35-44',
            'y4': list(admissions.all().values_list('age_35_to_44', flat=True).order_by('year')),
            'name5': '45-54',
            'y5': list(admissions.all().values_list('age_45_to_54', flat=True).order_by('year')),
            'name6': '55-64',
            'y6': list(admissions.all().values_list('age_55_to_64', flat=True).order_by('year')),
            'name7': '65-74',
            'y7': list(admissions.all().values_list('age_65_to_74', flat=True).order_by('year')),
            'name8': '75+',
            'y8': list(admissions.all().values_list('age_75_and_over', flat=True).order_by('year')),
            'name9': 'Unknown',
            'y9': list(admissions.all().values_list('age_unknown', flat=True).order_by('year'))
        }

        charttype = 'stackedAreaChart'
        extra = {
            'x_is_date': True,
            'x_axis_format': '%Y'
        }

    table_admissions = {}
    admissions_under_16 = admissions.values('year', 'age_under_16').order_by('year')
    admissions_16_24 = admissions.values('year', 'age_16_to_24').order_by('year')
    admissions_25_34 = admissions.values('year', 'age_25_to_34').order_by('year')
    admissions_35_44 = admissions.values('year', 'age_35_to_44').order_by('year')
    admissions_45_54 = admissions.values('year', 'age_45_to_54').order_by('year')
    admissions_55_64 = admissions.values('year', 'age_55_to_64').order_by('year')
    admissions_65_74 = admissions.values('year', 'age_65_to_74').order_by('year')
    admissions_75_and_over = admissions.values('year', 'age_75_and_over').order_by('year')
    admissions_unknown = admissions.values('year', 'age_unknown').order_by('year')
    admissions_total = admissions.values('year', 'total').order_by('year')

    for sur in itertools.chain(admissions_under_16, admissions_16_24, admissions_25_34, admissions_35_44, admissions_45_54, admissions_55_64, admissions_65_74, admissions_75_and_over, admissions_unknown, admissions_total):
        if sur['year'] in table_admissions:
            table_admissions[sur['year']].update(sur)
        else:
            table_admissions[sur['year']] = dict(sur)

    table = AdmissionsByAgeTable(table_admissions.values())
    RequestConfig(request).configure(table)

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'extra': extra,
        'surgery_table': table
    }

#    return JsonResponse([{'key': 'Admissions By Age',
#        'values': [{"label": chartdata["name1"], "value": chartdata["y1"]}]
#        }], safe=False)

    return render(request, 'diagnosis/admissions-by-age.html', data)


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
