import numpy as np
import matplotlib.pyplot as plt
import csv


Vdd_consts = np.asarray([0.2, 0.4, 1])


with open('data12.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))
    
Xrange = np.asarray(data[1:,0]).astype('float')
Yrange = np.asarray(data[1:,1]).astype('float') 
plt.plot(Xrange, Yrange*1e6)
plt.xlabel('V_gs')
plt.ylabel('I_d [uA]')
plt.title('Cadence V_gs sweep Vds: 0.4')
plt.show()