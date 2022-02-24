# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:57:02 2022

@author: david.inman
"""

from datetime import datetime

def dtToSsep(date_time_obj):
    # for 2.7 compatability
    timestamp = (date_time_obj - datetime(1970, 1, 1)).total_seconds()
    return int(timestamp)

def prettyTimetoSsep(dt_string):
    date_time_obj = datetime.strptime(dt_string, '%Y/%m/%d %H:%M:%S')
    return dtToSsep(date_time_obj)

def getSsep():
    date_time_obj = datetime.now()
    return int(dtToSsep(date_time_obj))
