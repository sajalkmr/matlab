#Exponential curve y=e^x

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.001) #takes value btw -10 ans 10 with a step length of 0.001

y = np.exp(x) #expo function

plt.plot(x,y, color="red") #plotting
plt.title("Exponential curve")
plt.grid() #display grid
plt.show() #show plot


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.001) #takes value btw -10 ans 10 with a step length of 0.001

y1 = np.sin(x) #expo function 
y2 = np.cos(x)


plt.plot(x,y1,x,y2) #plotting
plt.title("Sine & Cosine Curve")
plt.xlabel("values of x")
plt.ylabel("values of sinx &cosx ")
plt.grid() #display grid
plt.show() #show plot