#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from sharing import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
]
