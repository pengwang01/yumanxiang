from django.conf.urls import url
from . import views

app_name = 'ymx'  # this is the namespace

urlpatterns = [
    # /ymx/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[-\w]+)/$', views.IndexView.as_view(), name='index'),

]