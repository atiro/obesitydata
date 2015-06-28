try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views
from models import AdmissionsByGender

# place app url patterns here

urlpatterns = [
    url(r'^admissions/age$', views.admissions_by_age, name='admissions_by_age'),
    url(r'^admissions/age/(?P<year>\d{4})$', views.admissions_by_age, name='admissions_by_age'),
    url(r'^admissions/gender/primary$', views.admissions_by_gender, {'diagnosis': AdmissionsByGender.PRIMARY}, name='admissions_by_gender_primary'),
    url(r'^admissions/gender/primary/(?P<year>\d{4})$', views.admissions_by_gender, {'diagnosis': AdmissionsByGender.PRIMARY}, name='admissions_by_gender_primary'),
    url(r'^admissions/gender/secondary$', views.admissions_by_gender, {'diagnosis': AdmissionsByGender.SECONDARY}, name='admissions_by_gender_secondary'),
    url(r'^admissions/gender/secondary/(?P<year>\d{4})$', views.admissions_by_gender, {'diagnosis': AdmissionsByGender.SECONDARY}, name='admissions_by_gender_secondary'),
    url(r'^surgery/gender$', views.surgery_gender_england, name='surgery_by_gender'),
    url(r'^surgery/gender/(?P<year>\d{4})$', views.surgery_gender_england, name='surgery_by_gender')
]
