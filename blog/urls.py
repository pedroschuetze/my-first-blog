# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:57:31 2020

@author: Asus Notebook
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]