#############################
# Author: Chen Bi
# Date: 18 May 2020
#############################

from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('view_template/', views.staticpage, name='template-map'),
	path('sent/', views.send_off, name='sent'),
	path('db_update/', views.get_latest_email_data),
	re_path(r'^email/(?P<strategy>[a-z]{1})/$', views.email_strategy_select),
	re_path(r'^template/(?P<template>[0-9]{1})/$', views.email_template),
]