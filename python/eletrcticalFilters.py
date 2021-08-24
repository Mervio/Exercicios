#############Filter for the class of Electrical filters at UFCG##############
#Just change the return equation, to get the plot of other types of filters#
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

f0=1000;
def H(w):
 wc=2*3.14159*f0
 return (-w/wc)/(1-w/wc) #Equation
w = logspace(1,5) # frequencies from 10**1 to 10**5
fig, mag = plt.subplots(2,sharex=True)
plt.xscale('log')
#///MAGNITUDE///
mag[0].plot(w, 20*log10(abs(H(w))));
mag[0].set( ylabel='Ganho(db)',
 title='Filtro 6, wc=6283.2rad/s')
mag[0].grid()
#///PHASE///
mag[1].plot(w, np.angle(H(w)));
mag[1].set(xlabel='w(hz)', ylabel='phase(°)')
mag[1].grid()
fig.savefig("mag.png")
plt.show()