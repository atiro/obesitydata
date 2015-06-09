try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views

# place app url patterns here

urlpatterns = [
        url(r'^annual/england/(?P<year>\d{4})$', views.annual_england)
]
