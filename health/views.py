from datetime import datetime
import itertools

from django.shortcuts import render
from django.db.models import F
from django.http import JsonResponse

from django_tables2 import RequestConfig

from .models import HealthBMI, HealthActivity, HealthFruitVeg, HealthHealth

from .tables import BMIByGenderTable, ActivityByGenderTable, FruitVegByGenderTable, HealthByGenderTable


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

    if "application/json" in request.META.get('HTTP_ACCEPT'):
        return JsonResponse([{"key": "Meets", "values": zip(chartdata['x'], chartdata['y1']) }, {"key": "Some", "values": zip(chartdata['x'], chartdata['y2'])}, {"key": "Low", "values": zip(chartdata['x'], chartdata['y3'])}], safe=False)

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

def diet_by_gender(request, gender="all", age=HealthFruitVeg.AGE_ALL, year=None, portions=None):

    if gender == "male":
        gender = HealthFruitVeg.MALE
    elif gender == "female":
        gender = HealthFruitVeg.FEMALE
    else:
        gender = HealthFruitVeg.ALL

    if age == "16-24":
        age = HealthFruitVeg.AGE_16_TO_24
    elif age == "25-34":
        age = HealthFruitVeg.AGE_25_TO_34
    elif age == "35-44":
        age = HealthFruitVeg.AGE_35_TO_44
    elif age == "45-54":
        age = HealthFruitVeg.AGE_45_TO_54
    elif age == "55-64":
        age = HealthFruitVeg.AGE_55_TO_64
    elif age == "65-74":
        age = HealthFruitVeg.AGE_65_TO_74
    elif age == "75+":
        age = HealthFruitVeg.AGE_75_PLUS
    else:
        age = HealthFruitVeg.AGE_ALL

    if year is not None:
        fruitveg = HealthFruitVeg.objects.all().filter(year=year).filter(gender=gender).filter(age=age)
    else:
        fruitveg = HealthFruitVeg.objects.all().filter(age=age)


    chartdata = {
        'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in fruitveg.values_list('year', flat=True).distinct().order_by('year')],
        'name1': 'None',
        'y1': fruitveg.filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_NONE).values_list('percentage', flat=True).order_by('year'),
        'name2': 'Less than 1',
        'y2': fruitveg.filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_LESS_1).values_list('percentage', flat=True).order_by('year'),
        'name3': 'Between 1 and 2',
        'y3': fruitveg.filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_LESS_2).values_list('percentage', flat=True).order_by('year'),
        'name4': 'Between 2 and 3',
        'y4': fruitveg.filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_LESS_3).values_list('percentage', flat=True).order_by('year'),
        'name5': 'Between 3 and 4',
        'y5': fruitveg.filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_LESS_4).values_list('percentage', flat=True).order_by('year'),
        'name6': 'Between 4 and 5',
        'y6': fruitveg.filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_LESS_5).values_list('percentage', flat=True).order_by('year'),
        'name7': 'Over 5',
        'y7': fruitveg.filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_MORE_5).values_list('percentage', flat=True).order_by('year')
    }

    if "application/json" in request.META.get('HTTP_ACCEPT'):
        return JsonResponse([{"key": "None", "values": zip(chartdata['x'], chartdata['y1']) }, {"key": "0-1", "values": zip(chartdata['x'], chartdata['y2']) }, {"key": "1-2", "values": zip(chartdata['x'], chartdata['y3']) }, {"key": "2-3", "values": zip(chartdata['x'], chartdata['y4']) }, {"key": "3-4", "values": zip(chartdata['x'], chartdata['y5']) }, {"key": "4-5", "values": zip(chartdata['x'], chartdata['y6']) }, {"key": "Over 5", "values": zip(chartdata['x'], chartdata['y7'])}], safe=False)

    charttype = 'stackedAreaChart'
    chartcontainer = 'stackedarea_container'

    table_fruitveg = {}
    fruitveg_none = fruitveg.values('year').annotate(fruitveg_none=F('percentage')).filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_NONE)
    fruitveg_less_1 = fruitveg.values('year').annotate(fruitveg_less_1=F('percentage')).filter(gender=gender).filter(fruitveg=HealthFruitVeg.FRUITVEG_LESS_1)
#    female_admissions = admissions.values('year').annotate(female_admissions=F('admissions')).filter(gender='F')
#    unknown_admissions = admissions.values('year').annotate(unknown_admissions=F('admissions')).filter(gender='U')
#    total_admissions = admissions.values('year').annotate(total_admissions=Sum('admissions'))

    for sur in itertools.chain(fruitveg_none, fruitveg_less_1):
        if sur['year'] in table_fruitveg:
            table_fruitveg[sur['year']].update(sur)
        else:
            table_fruitveg[sur['year']] = dict(sur)

    table = FruitVegByGenderTable(table_fruitveg.values())
    RequestConfig(request).configure(table)

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'surgery_table': table,
        'title': 'Fruit & Veg',
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%Y',
            'y_axis_format': '%.0f'
        },
    }

    return render(request, 'health/diet-by-gender.html', data)

def health_by_gender(request, gender="all", year=None):

    if gender == "male":
        gender = HealthHealth.MALE
    elif gender == "female":
        gender = HealthHealth.FEMALE
    else:
        gender = HealthHealth.ALL

    if year is not None:
        health = HealthHealth.objects.all().filter(year=year).filter(gender=gender)
    else:
        health = HealthHealth.objects.all()

    chartdata = {
        'x': [int(datetime(x, 1, 1).strftime('%s'))*1000 for x in health.values_list('year', flat=True).distinct().order_by('year')],
        'name1': 'Very Good/Good',
        'y1': health.filter(gender=gender).filter(health=HealthHealth.HEALTH_VG).values_list('percentage', flat=True).order_by('year'),
        'name2': 'Very Bad/Bad',
        'y2': health.filter(gender=gender).filter(health=HealthHealth.HEALTH_VB).values_list('percentage', flat=True).order_by('year'),
        'name3': 'At least one longstanding illness',
        'y3': health.filter(gender=gender).filter(health=HealthHealth.HEALTH_ILL).values_list('percentage', flat=True).order_by('year'),
        'name4': 'Acute sickness',
        'y4': health.filter(gender=gender).filter(health=HealthHealth.HEALTH_SICK).values_list('percentage', flat=True).order_by('year'),
    }

    charttype = 'stackedAreaChart'
    chartcontainer = 'stackedarea_container'

    table_health = {}
    health_vg = health.values('year').annotate(health_vg=F('percentage')).filter(gender=gender).filter(health=HealthHealth.HEALTH_VG)
    health_vb = health.values('year').annotate(health_vb=F('percentage')).filter(gender=gender).filter(health=HealthHealth.HEALTH_VB)
#    female_admissions = admissions.values('year').annotate(female_admissions=F('admissions')).filter(gender='F')
#    unknown_admissions = admissions.values('year').annotate(unknown_admissions=F('admissions')).filter(gender='U')
#    total_admissions = admissions.values('year').annotate(total_admissions=Sum('admissions'))

    for sur in itertools.chain(health_vg, health_vb):
        if sur['year'] in table_health:
            table_health[sur['year']].update(sur)
        else:
            table_health[sur['year']] = dict(sur)

    table = HealthByGenderTable(table_health.values())
    RequestConfig(request).configure(table)

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'surgery_table': table,
        'title': 'Health',
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%Y',
            'y_axis_format': '%.0f'
        },
    }

    return render(request, 'health/health-by-gender.html', data)
