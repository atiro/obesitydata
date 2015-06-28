try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views

# place app url patterns here

urlpatterns = [
    url(r'^admissions/age$', views.admissions_by_age, name='admissions-by-age'),
    url(r'^admissions/age/(?P<year>\d{4})$', views.admissions_by_age, name='admissions-y-age'),
    url(r'^admissions/gender$', views.admissions_by_gender),
    url(r'^admissiions/gender/(?P<year>\d{4})$', views.admissions_by_gender),
    url(r'^surgery/gender$', views.surgery_gender_england, name='surgery-by-gender'),
    url(r'^surgery/gender/(?P<year>\d{4})$', views.surgery_gender_england, name='surgery-by-gender')
]
