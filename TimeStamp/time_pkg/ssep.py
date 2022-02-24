# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:28:24 2022

@author: david.inman
"""

from datetime import datetime

def dtToPrettyTime(date_time_obj):
    dt_string = date_time_obj.strftime('%Y/%m/%d %H:%M:%S')
    return dt_string

def ssepToPrettyTime(ssep):
    date_time_obj = datetime.utcfromtimestamp(ssep)
    return dtToPrettyTime(date_time_obj)

def getPrettyTime():
    date_time_obj = datetime.now()
    return dtToPrettyTime(date_time_obj)

