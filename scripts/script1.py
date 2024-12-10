# This is an exemplary script file.
import numpy as np
import scipy as sc 
import matplotlib.pyplot as plt
import os

curr_dir = os.getcwd()

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
plt.savefig(curr_dir + '/sin_plot.png')