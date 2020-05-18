#############################
# Author: Chen Bi
# Date: 18 May 2020
#############################

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('sent/', views.send_off, name='sent'),
]
