from django.conf.urls import url
from . import views

app_name = 'ymx'  # this is the namespace

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

]