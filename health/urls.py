try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views

# place app url patterns here

urlpatterns = [
    url(r'^bmi/$', views.bmi_by_gender,
        name='bmi'),
    url(r'^bmi/(?P<gender>(male|female|all))$', views.bmi_by_gender,
        name='bmi_by_gender'),
    url(r'^bmi/(?P<gender>(male|female|all))/(?P<age>[\d\-]+)$', views.bmi_by_gender,
        name='bmi_by_gender_age'),

    url(r'^activity/$', views.activity_by_gender,
        name='activity'),
    url(r'^activity/(?P<gender>(male|female|all))$', views.activity_by_gender,
        name='activity_by_gender'),
    url(r'^activity/(?P<gender>(male|female|all))/(?P<age>[\d\-]+)$', views.activity_by_gender,
        name='activity_by_gender_age'),

    url(r'^diet/$', views.diet_by_gender,
        name='diet'),
    url(r'^diet/(?P<gender>(male|female|all))$', views.diet_by_gender,
        name='diet_by_gender'),
    url(r'^diet/(?P<gender>(male|female|all))/(?P<age>[\d\-]+)$', views.diet_by_gender,
        name='diet_by_gender_age'),

    url(r'^health/$', views.health_by_gender,
        name='health'),
    url(r'^health/(?P<gender>(male|female|all))$', views.health_by_gender,
        name='health_by_gender')
]
