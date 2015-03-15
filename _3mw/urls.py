from django.conf.urls import patterns, include, url
from django.contrib import admin
from _3mw_app.views import b_test

urlpatterns = patterns('',
                       url(r'^b_test/',
                           b_test,
                           name='b_test'),
                       url(r'^admin/',
                           include(admin.site.urls)))
