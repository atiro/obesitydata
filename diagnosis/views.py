from django.shortcuts import render_to_response

from diagnosis.models import Admissions

def annual_england(request, year=None):

    if year not None:
       admissions = Admissions.objects.all().filter(year=year)

        return render_to_response('diagnosis/annual.html', {'admissions': admissions})
    else:
        admissions = Admissions.objects.all()

        data = {
                'x': Admissions.objects.all().aggregate(year),
                'name1': 'Male', 'y1': 

        return render_to_response('diagnosis/england.html', {'data': data})

# Create your views here.
