from datetime import datetime
import itertools

from django.shortcuts import render
from django.db.models import F, Sum

from django_tables2 import RequestConfig

from models import HealthBMI, HealthActivity

from tables import BMIByGenderTable, ActivityByGenderTable


def bmi_by_gender(request, gender="all", age=HealthBMI.AGE_ALL, year=None):

    if gender == "male":
        gender = HealthBMI.MALE
    elif gender == "female":
        gender = HealthBMI.FEMALE
    else:
        gender = HealthBMI.ALL

    if age == "16-24":
        age = HealthBMI.AGE_16_TO_24
    elif age == "25-34":
        age = HealthBMI.AGE_25_TO_34
    elif age == "35-44":
        age = HealthBMI.AGE_35_TO_44
    elif age == "45-54":
        age = HealthBMI.AGE_45_TO_54
    elif age == "55-64":
        age = HealthBMI.AGE_55_TO_64
    elif age == "65-74":
        age = HealthBMI.AGE_65_TO_74
    elif age == "75+":
        age = HealthBMI.AGE_75_PLUS
    else:
        age = HealthBMI.AGE_ALL

    if year is not None:
        bmi = HealthBMI.objects.all().filter(year=year).filter(gender=gender).filter(age=age)
    else:
        bmi = HealthBMI.objects.all().filter(age=age)

    chartdata = {
        'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in bmi.values_list('year', flat=True).distinct().order_by('year')],
        'name1': 'Underweight',
        'y1': bmi.filter(gender=gender).filter(bmi=HealthBMI.BMI_UNDERWEIGHT).values_list('percentage', flat=True).order_by('year'),
        'name2': 'Normal',
        'y2': bmi.filter(gender=gender).filter(bmi=HealthBMI.BMI_NORMAL).values_list('percentage', flat=True).order_by('year'),
        'name3': 'Overweight',
        'y3': bmi.filter(gender=gender).filter(bmi=HealthBMI.BMI_OVERWEIGHT).values_list('percentage', flat=True).order_by('year'),
        'name4': 'Obese',
        'y4': bmi.filter(gender=gender).filter(bmi=HealthBMI.BMI_OBESE).values_list('percentage', flat=True).order_by('year')
    }

    charttype = 'stackedAreaChart'
    chartcontainer = 'stackedarea_container'

    table_bmi = {}
    underweight_bmi = bmi.values('year').annotate(underweight_bmi=F('percentage')).filter(gender=gender).filter(bmi=HealthBMI.BMI_UNDERWEIGHT)
    normal_bmi = bmi.values('year').annotate(normal_bmi=F('percentage')).filter(gender=gender).filter(bmi=HealthBMI.BMI_NORMAL)
    overweight_bmi = bmi.values('year').annotate(overweight_bmi=F('percentage')).filter(gender=gender).filter(bmi=HealthBMI.BMI_OVERWEIGHT)
    obese_bmi = bmi.values('year').annotate(obese_bmi=F('percentage')).filter(gender=gender).filter(bmi=HealthBMI.BMI_OBESE)
    morbidly_bmi = bmi.values('year').annotate(morbidly_bmi=F('percentage')).filter(gender=gender).filter(bmi=HealthBMI.BMI_MORBIDLY_OBESE)
#    female_admissions = admissions.values('year').annotate(female_admissions=F('admissions')).filter(gender='F')
#    unknown_admissions = admissions.values('year').annotate(unknown_admissions=F('admissions')).filter(gender='U')
#    total_admissions = admissions.values('year').annotate(total_admissions=Sum('admissions'))

    for sur in itertools.chain(underweight_bmi, normal_bmi, overweight_bmi, obese_bmi, morbidly_bmi):
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
        'title': 'BMI (Male & Female, 18-75)',
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%Y',
            'y_axis_format': '%.0f'
        },
    }

    return render(request, 'health/bmi-by-gender.html', data)


def activity_by_gender(request, gender="all", age=HealthActivity.AGE_ALL, year=None):

    if gender == "male":
        gender = HealthActivity.MALE
    elif gender == "female":
        gender = HealthActivity.FEMALE
    else:
        gender = HealthActivity.ALL

    if age == "16-24":
        age = HealthActivity.AGE_16_TO_24
    elif age == "25-34":
        age = HealthActivity.AGE_25_TO_34
    elif age == "35-44":
        age = HealthActivity.AGE_35_TO_44
    elif age == "45-54":
        age = HealthActivity.AGE_45_TO_54
    elif age == "55-64":
        age = HealthActivity.AGE_55_TO_64
    elif age == "65-74":
        age = HealthActivity.AGE_65_TO_74
    elif age == "75+":
        age = HealthActivity.AGE_75_PLUS
    else:
        age = HealthActivity.AGE_ALL

    if year is not None:
        activity = HealthActivity.objects.all().filter(year=year).filter(gender=gender).filter(age=age)
    else:
        activity = HealthActivity.objects.all().filter(age=age)

    chartdata = {
        'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in activity.values_list('year', flat=True).distinct().order_by('year')],
        'name1': 'Meets',
        'y1': activity.filter(gender=gender).filter(activity=HealthActivity.ACTIVITY_MEETS).values_list('percentage', flat=True).order_by('year'),
        'name2': 'Some',
        'y2': activity.filter(gender=gender).filter(activity=HealthActivity.ACTIVITY_SOME).values_list('percentage', flat=True).order_by('year'),
        'name3': 'Low',
        'y3': activity.filter(gender=gender).filter(activity=HealthActivity.ACTIVITY_LOW).values_list('percentage', flat=True).order_by('year')
    }

    charttype = 'stackedAreaChart'
    chartcontainer = 'stackedarea_container'

    table_activity = {}
    activity_meets = activity.values('year').annotate(activity_meets=F('percentage')).filter(gender=gender).filter(activity=HealthActivity.ACTIVITY_MEETS)
    activity_some = activity.values('year').annotate(activity_some=F('percentage')).filter(gender=gender).filter(activity=HealthActivity.ACTIVITY_SOME)
    activity_low = activity.values('year').annotate(activity_low=F('percentage')).filter(gender=gender).filter(activity=HealthActivity.ACTIVITY_LOW)
#    female_admissions = admissions.values('year').annotate(female_admissions=F('admissions')).filter(gender='F')
#    unknown_admissions = admissions.values('year').annotate(unknown_admissions=F('admissions')).filter(gender='U')
#    total_admissions = admissions.values('year').annotate(total_admissions=Sum('admissions'))

    for sur in itertools.chain(activity_meets, activity_some, activity_low):
        if sur['year'] in table_activity:
            table_activity[sur['year']].update(sur)
        else:
            table_activity[sur['year']] = dict(sur)

    table = ActivityByGenderTable(table_activity.values())
    RequestConfig(request).configure(table)

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'surgery_table': table,
        'title': 'BMI (Male & Female, 18-75)',
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%Y',
            'y_axis_format': '%.0f'
        },
    }

    return render(request, 'health/activity-by-gender.html', data)
