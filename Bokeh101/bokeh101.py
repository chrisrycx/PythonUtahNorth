'''
Code for Bokeh 101
- Chris Cox, 5/15/2019
'''

#Imports: numpy, matplotlib, bokeh
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row 

#Generate some data for graphing
x = np.linspace(0,2*np.pi,50)
y = np.sin(x)
y2 = np.cos(x)
y3 = -1/6*x + 1

#Plot using matplotlib
#plt.plot(x,y,'b',x,y2,'r',x,y3,'k')
#plt.show()

#Basic plot using Bokeh
#output_file("basics.html") #Output to static HTML file
#p = figure(title="Basic Example", x_axis_label='x', y_axis_label='y')
#p.line(x, y, line_width=2) # add a line renderer
#show(p) # show the results

#Layout and share axis
output_file("layout.html") #Output to static HTML file
p = figure(title="Layout Example", x_axis_label='x', y_axis_label='y')
p.line(x, y, color="blue", line_width=2) # add a line renderer
p.line(x, y2, color="red", line_width=2)
p2 = figure(title="Layout Example 2", x_axis_label='x', y_axis_label='y',
            x_range=p.x_range)
p2.line(x, y3, color="red", line_width=2)
show(row(p,p2)) # show the results