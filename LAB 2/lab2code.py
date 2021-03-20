#task 1 part 1 sweep

import numpy as np
import matplotlib.pyplot as plt
import csv


with open('t1_p1.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))


Xrange1 = np.asarray(data[1:,0]).astype('float')
Yrange1 = np.asarray(data[1:,1]).astype('float') 
plt.savefig('t1_p1.png')
fig1 = plt.plot(Xrange1, Yrange1)
plt.xlabel('V_I')
plt.ylabel('V_o')
plt.plot([0, 0.6], [0.6, 0.6], color='r', linestyle='--', linewidth=2)
plt.plot([0.6, 0.6], [0, 0.6], color='r', linestyle='--', linewidth=2)
plt.title('CMOS inverter scaled pFET width')
plt.savefig('t1_p1.png', dpi=100)
plt.show()

##########################################################################

#Task 2, computing voltage gain
key2 = np.asarray(np.where(0.6 <= Xrange1)).astype('int')
print("inverter 1 Whats my intial V_I?:", Xrange1[key2[0,0]])
print("inverter 1 Voltage gain:", (Yrange1[key2[0,1]] - Yrange1[key2[0,0]])/(Xrange1[key2[0,1]] - Xrange1[key2[0,0]]))

##########################################################################
#task 1 part 2 sweep

import numpy as np
import matplotlib.pyplot as plt
import csv


with open('t1_p2.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))


Xrange2 = np.asarray(data[1:,0]).astype('float')
Yrange2 = np.asarray(data[1:,1]).astype('float') 
plt.savefig('t1_p1.png')
fig1 = plt.plot(Xrange2, Yrange2)
plt.xlabel('V_I')
plt.ylabel('V_o')
plt.plot([0, 0.6], [0.6, 0.6], color='r', linestyle='--', linewidth=2)
plt.plot([0.6, 0.6], [0, 0.6], color='r', linestyle='--', linewidth=2)
plt.title('CMOS inverter with inverted geometries')
plt.savefig('t1_p2.png', dpi=100)
plt.show()
##########################################################################

#Task 2, computing voltage gain
key3 = np.asarray(np.where(0.6 <= Xrange2)).astype('int')
print("Inverter 2 Whats my intial V_I?:", Xrange2[key3[0,0]])
print("Inverter 2 Voltage gain:", (Yrange2[key3[0,1]] - Yrange2[key3[0,0]])/(Xrange2[key3[0,1]] - Xrange2[key3[0,0]]))
##########################################################################

#task 3 part 1 sweep

import numpy as np
import matplotlib.pyplot as plt
import csv


with open('t3_p1.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))


Xrange31 = np.asarray(data[1:,0]).astype('float')
Yrange31 = np.asarray(data[1:,1]).astype('float') 
plt.savefig('t1_p1.png')
fig1 = plt.plot(Xrange31[:220], Yrange31[:220])
plt.xlabel('time [S]')
plt.ylabel('V_o')
plt.title('CMOS inverter 1 in series')
plt.savefig('t3.png', dpi=100)
plt.show()
##########################################################################
#task 3 part 2 sweep

import numpy as np
import matplotlib.pyplot as plt
import csv


with open('t3_p2.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))


Xrange32 = np.asarray(data[1:,0]).astype('float')
Yrange32 = np.asarray(data[1:,1]).astype('float') 
plt.savefig('t1_p1.png')
fig1 = plt.plot(Xrange32[:220], Yrange32[:220])
plt.xlabel('time [S]')
plt.ylabel('V_o')
plt.title('CMOS inverter 2 in series')
plt.savefig('t3.png', dpi=100)
plt.show()
##########################################################################
Vomax32 = np.asarray(np.where(1.2 <= Yrange32)).astype('int')
Vomin32 = np.asarray(np.where(0.1 >= Yrange32)).astype('int')
print(Vomax32.shape)
print(Vomin32.shape)
Vomax31 = np.asarray(np.where(1.2 <= Yrange31)).astype('int')
Vomin31 = np.asarray(np.where(0.1 >= Yrange31)).astype('int')
print(Vomax31.shape)
print(Vomin31.shape)