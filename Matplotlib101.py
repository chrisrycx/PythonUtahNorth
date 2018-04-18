# -*- coding: utf-8 -*-
'''
Utah Python North - 5/18/2018
Chris Cox - @chrisrycx, chrisrycx@github.io 

Matplotlib 101:
- Website - www.matplotlib.org
    - Whats in a name?
    - NUMFOCUS
    - Tutorials
    - Capabilities
- Installation
    - pip install matplotlib
    - import matplotlib.pyplot as plt
    - graphics backend??
- Basics
    - plot
    - subplot
    - using with numpy and pandas
- Examples
    - Jupyter notebook widget
    - Snow temperature animation

   
'''

'''
Plot
- Basic plot with list
    - Interaction with plot
- Multiple lines with numpy arrays
- Pandas dataframe plot
'''

#Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

#x = [1,2,3,4]
#y = [5,6,7,8]

#x = np.linspace(0,2*np.pi)
#y = np.sin(x)
#y2 = np.cos(x)

#x = [dt.datetime(2018,4,18,18,0),dt.datetime(2018,4,18,18,15),dt.datetime(2018,4,18,18,20),dt.datetime(2018,4,18,18,55)]
#y = [5,6,7,8]

#plt.plot(x,y,'r',x,y2,'b')
#plt.show()

#Pandas stuff
#Create a dataframe
dates = pd.DatetimeIndex(start='4/17/2018',end='4/18/2018',freq='H')
vals = np.linspace(0,10*np.pi,num=dates.size)
cols = {'mydata':np.cos(vals)}
data = pd.DataFrame(cols,index=dates)

data.plot()
plt.show()
