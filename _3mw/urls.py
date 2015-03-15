from django.conf.urls import patterns, include, url
from django.contrib import admin
from _3mw_app.views import SitesList, SitesDetail, SummaryList, SummaryListAverage

urlpatterns = patterns('',
                       # List View for Sites Page
                       # matches /, /sites/, /sites
                       url(r'(^sites/?$)|(^/?$)',
                           SitesList.as_view(),
                           name='sites'),

                       # Detail View for Sites
                       # matches /sites/#, /sites/#/
                       url(r'^sites/(?P<pk>\d+)/?$',
                           SitesDetail.as_view(),
                           name='sites_detail'),

                       # List View for Summary Page
                       # matches /summary, /summary/
                       url(r'^summary/?$',
                           SummaryList.as_view(),
                           name='summary'),

                       # List View for Summary Average Page
                       # matches /summary-average, /summary-average/
                       url(r'^summary-average/?$',
                           SummaryListAverage.as_view(),
                           name='summary_avg'),

                       # Admin
                       url(r'^admin/',
                           include(admin.site.urls)))
