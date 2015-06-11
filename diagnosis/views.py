from django.shortcuts import render_to_response

from diagnosis.models import Admissions


def annual_england(request, year=None):

    if year is not None:
        admissions = Admissions.objects.all().filter(year=year)

        return render_to_response('diagnosis/annual.html',
                                  {'admissions': admissions})
    else:
        admissions = Admissions.objects.all()

        chartdata = {
            'x': Admissions.objects.values_list('year', flat=True).distinct().order_by('year'),
            'name1': 'Male',
            'y1': Admissions.objects.filter(gender='M').values_list('admissions', flat=True).order_by('year'),
            'name2': 'Female',
            'y2': Admissions.objects.filter(gender='F').values_list('admissions', flat=True).order_by('year'),
            'name3': 'Unknown',
            'y2': Admissions.objects.filter(gender='U').values_list('admissions', flat=True).order_by('year'),
        }

        charttype = 'stackedAreaChart'
        data = {
            'charttype': charttype,
            'chartdata': chartdata
        }

        return render_to_response('diagnosis/england.html', {'data': data})

# Create your views here.
