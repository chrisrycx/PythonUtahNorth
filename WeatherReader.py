# -*- coding: utf-8 -*-

"""
Try to import and read crawford point weather data
8/31/2017
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

#Load parameters
fname = 'CrawfordWeather_short.txt'
seper = ' '
skiplines = 14
headernames = ['station','year','Julian','pressure','windd1','windd2'
               ,'winds1','winds2','rh1','rh2','airT1','airT2']
               
#Date parse function
#dparse = lambda x, y: datetime.datetime.strptime(' '.join([x,y]), '%Y %j')

#Load the file
wdata = pd.read_table(fname,sep=seper,header=None,names=headernames,
                      skiprows=14)

wdata['datetimes'] = pd.to_datetime(wdata.year,format='%Y') + pd.to_timedelta((wdata['Julian']-1),unit='d')
wdata['dateclean'] = pd.DatetimeIndex(wdata.datetimes).round('1H')

airdata = wdata[['dateclean','airT1','airT2','Julian']]
                
airdata.index = airdata.dateclean

ax = airdata['1/1/2009':'12/31/2009'].plot(x='Julian',y='airT1')

#Create sin wave
freq = 1/360 #cycles per time
w = 2*np.pi*freq

t = np.linspace(0, 400, 100)
y = 15*np.sin(w*(t - 100)) - 15

ax.plot(t,y,'r')
plt.grid()