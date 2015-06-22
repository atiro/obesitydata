try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views

# place app url patterns here

urlpatterns = [
    url(r'^age/england$', views.age_england, name='admissions-by-age'),
    url(r'^age/england/(?P<year>\d{4})$', views.age_england, name='admissions-y-age'),
    url(r'^annual/england$', views.annual_england),
    url(r'^annual/england/(?P<year>\d{4})$', views.annual_england),
    url(r'^surgery/gender$', views.surgery_gender_england, name='surgery-by-gender'),
    url(r'^surgery/gender/(?P<year>\d{4})$', views.surgery_gender_england, name='surgery-by-gender')
]
