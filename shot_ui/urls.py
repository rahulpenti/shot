__author__ = 'root'
from django.conf.urls import patterns, url
import views
urlpatterns = patterns('',
    url(r'^$', views.main, name='Check'),

)