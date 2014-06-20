from django.conf.urls import patterms, url
from rango import views

urlpatterns = patterns('', url(r'^$', view.index, name = 'index'))