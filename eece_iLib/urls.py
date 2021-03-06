"""eece_iLib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from iLib.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^signup/$', signup),
    url(r'^dashboard/$', dashboard),
    url(r'^addbooks/', addbooks),
    url(r'^editbook/', editbook),
    url(r'^deletebook/', deletebook),
    url(r'^borrow/$', borrow),
    url(r'^cancel/$', cancel),
    url(r'^accept/$', accept),
    url(r'^returned/$', returned),
    url(r'^logs/$', logs),
    url(r'^search/$', search),
]
