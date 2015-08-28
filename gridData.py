# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:54:58 2015

@author: Wood
"""

# from mpl_toolkits.basemap import Basemap

import matplotlib.pyplot as plt
import os
from math import *
import numpy as np

def read_gridData(filename):
    rainfile = open(filename,"r")
    raindataI5 = rainfile.readlines()
    raindata = raindataI5[6:]

#raindata2 = pandas.read_csv(filename, skiprows=5,delimiter='\s+', index_col=False)
    rain2=np.zeros((290, 180))
    for j in range(0,len(raindata)):
        rain = raindata[j].split()
        for i in range(0,len(rain)):       
            rain2[j,i] = float(rain[i])
            
    return(rain2)


#filename = os.getcwd() + '\\Rainfall_2007-2011\\' + 'Rainfall_2007-01_ACTUAL.txt'

allfile = os.listdir(os.getcwd() + '\\Rainfall_2007-2011\\')

rainall=np.zeros((60,290, 180))

for i in range(0,len(allfile)):
    filename = os.getcwd() + '\\Rainfall_2007-2011\\' + allfile[i]
    rainMon = read_gridData(filename)
    rainall[i,:,:] = rainMon

plt.rcParams['figure.figsize'] = (16,12)
 
plt.imshow(rainall[20,:,:])


# plt.imshow(air[0,:,:])


