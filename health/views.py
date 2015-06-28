from datetime import datetime
import itertools

from django.shortcuts import render
from django.db.models import F, Sum

from django_tables2 import RequestConfig

from models import HealthBMI

from tables import BMIByGenderTable


def bmi_by_gender(request, gender=HealthBMI.ALL, year=None):

    if year is not None:
        bmi = HealthBMI.objects.all().filter(year=year).filter(gender=gender).filter(age=HealthBMI.AGE_ALL)
    else:
        bmi = HealthBMI.objects.all().filter(age=HealthBMI.AGE_ALL)

    chartdata = {
        'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in bmi.values_list('year', flat=True).distinct().order_by('year')],
        'name1': 'Male',
        'y1': bmi.filter(gender=HealthBMI.MALE).filter(age=HealthBMI.AGE_ALL).filter(bmi=HealthBMI.BMI_ALL).values_list('percentage', flat=True).order_by('year'),
        'name2': 'Female',
        'y2': bmi.filter(gender=HealthBMI.FEMALE).filter(age=HealthBMI.AGE_ALL).filter(bmi=HealthBMI.BMI_ALL).values_list('percentage', flat=True).order_by('year')
    }

    charttype = 'stackedAreaChart'
    chartcontainer = 'stackedarea_container'

    table_bmi = {}
    male_bmi = bmi.values('year').annotate(male_percentage=F('percentage')).filter(gender=HealthBMI.MALE)
#    female_admissions = admissions.values('year').annotate(female_admissions=F('admissions')).filter(gender='F')
#    unknown_admissions = admissions.values('year').annotate(unknown_admissions=F('admissions')).filter(gender='U')
#    total_admissions = admissions.values('year').annotate(total_admissions=Sum('admissions'))

    for sur in itertools.chain(male_bmi):
        if sur['year'] in table_bmi:
            table_bmi[sur['year']].update(sur)
        else:
            table_bmi[sur['year']] = dict(sur)

    table = BMIByGenderTable(table_bmi.values())
    RequestConfig(request).configure(table)

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'surgery_table': table,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%Y',
            'y_axis_format': '%.0f'
        }
    }

    return render(request, 'health/bmi-by-gender.html', data)
