# -*- coding: utf-8 -*-
"""
Created on 11 Mar 2023
@author: T.Barlow
SDEV 220 Spring 2023
Python Version 11
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
