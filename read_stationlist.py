# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:59:33 2015

@author: Wood
"""

def read_stationlist()
    f = open('stationList.txt', 'r')
    stations= f.readlines()
    stationsL = []
    for i in range(len(stations)):
        stationsL.append(stations[i].strip('\n'))
        
    return stationsL

