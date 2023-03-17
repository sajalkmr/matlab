import numpy as np
 
import matplotlib.pyplot as plt 
plt.axes(projection = 'polar')
 
r=3
 
rads = np.arange(0, (2*np.pi), 0.01)
 
#plotting the circle 
for i in rads:
    plt.polar(1, r, "g.")

 

 
plt.show()




from pylab import *
theta=linspace(0,2*np.pi,1000)
r1=5+5*cos(theta)
polar(theta,r1,"g")
show()