try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views

# place app url patterns here

urlpatterns = [
    url(r'^bmi/gender$', views.bmi_by_gender,
        name='bmi_by_gender')
]
