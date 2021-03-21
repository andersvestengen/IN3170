#task 1 part 1 sweep
#task 1 part 1 sweep

import numpy as np
import matplotlib.pyplot as plt
import csv


with open('t1_p1.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))


Xrange1 = np.asarray(data[1:,0]).astype('float')
Yrange1 = np.asarray(data[1:,1]).astype('float') 
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
key3 = np.asarray(np.where(0.6 <= Xrange2)).astype('int')
print("Inverter 2Whats my intial V_I?:", Xrange2[key3[0,0]])
print("Inverter 2Voltage gain:", (Yrange2[key3[0,1]] - Yrange2[key3[0,0]])/(Xrange2[key3[0,1]] - Xrange2[key3[0,0]]))

##########################################################################
#task 1 part 2 sweep

with open('t1_p2.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))


Xrange2 = np.asarray(data[1:,0]).astype('float')
Yrange2 = np.asarray(data[1:,1]).astype('float') 
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


with open('t3_inverter1.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))


Xrange31 = np.asarray(data[1:,0]).astype('float')
Yrange31 = np.asarray(data[1:,1]).astype('float') 
fig1 = plt.plot(Xrange31, Yrange31)
plt.xlabel('time [S]')
plt.ylabel('V_o')
plt.title('CMOS inverters 1 in series')
plt.savefig('t3_p1.png', dpi=100)
plt.show()
##########################################################################
#task 3 part 2 sweep

with open('t3_inverter2.csv')as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))

thing = int(0.5*int(len(Xrange32)))
Xrange32 = np.asarray(data[1:,0]).astype('float')
Yrange32 = np.asarray(data[1:,1]).astype('float') 
fig1 = plt.plot(Xrange32, Yrange32)
plt.xlabel('time [S]')
plt.ylabel('V_o')
plt.title('CMOS inverters 2 in series')
plt.savefig('t3_p2.png', dpi=100)
plt.show()
##########################################################################

thing = int(0.5*int(len(Xrange32)))
Vomax32 = np.asarray(np.where(0 < Yrange32)).astype('int')
Vomin32 = np.asarray(np.where(0.6 <= Yrange32)).astype('int')
Vomax31 = np.asarray(np.where(0 < Yrange31)).astype('int')
Vomin31 = np.asarray(np.where(0.6 <= Yrange31)).astype('int')
# part 2
Vomax322 = np.asarray(np.where(1.2 <= Yrange32[thing:])).astype('int')
Vomin322 = np.asarray(np.where(0.6 > Yrange32[thing:])).astype('int')
Vomax311 = np.asarray(np.where(1.2 <= Yrange31[thing:])).astype('int')
Vomin311 = np.asarray(np.where(0.6 > Yrange31[thing:])).astype('int')


print(Yrange32[Vomin32[0,0]])
print(Vomin32[0,0])
print(Yrange32[Vomax32[0,0]])
print(Vomax32[0,0])
print(" ")
print(Yrange31[Vomin31[0,0]])
print(Vomin31[0,0])
print(Yrange31[Vomax31[0,0]])
print(Vomax31[0,0])


print(" ")
print(Yrange32[Vomax322[0,0]+thing])
print(Vomax322[0,0]+thing)
print(Yrange32[Vomin322[0,0]+thing])
print(Vomin322[0,0]+thing)
print(" ")
print(Yrange31[Vomax311[0,0]+thing])
print(Vomax311[0,0]+thing)
print(Yrange31[Vomin311[0,0]+thing])
print(Vomin311[0,0]+thing)
print(" ")


t_PLH1 = Xrange32[Vomin32[0,0]] - Xrange32[Vomax32[0,0]]
t_PHL1 = Xrange32[Vomin322[0,0]+thing] - Xrange32[Vomax322[0,0]+thing]


t_PLH2 = Xrange31[Vomin31[0,0]] - Xrange31[Vomax31[0,0]]
t_PHL2 = Xrange31[Vomin311[0,0]+thing] - Xrange31[Vomax311[0,0]+thing]

print("inverter1 LH, HL", t_PLH1*1e12, t_PHL1*1e12, "p S (pico seconds)")
print("inverter2 LH, HL", t_PLH2*1e12, t_PHL2*1e12, "p S (pico seconds)")
print(" ")
tp1 = 0.5*(t_PHL1 + t_PLH1)
tp2 = 0.5*(t_PHL2 + t_PLH2)
print("tp inverter1:", tp1*1e12, "p S (pico seconds)")
print("tp inverter2:", tp2*1e12, "p S (pico seconds)")
print(" ")
print("tp ratio inv2/inv1:", tp1/tp2, "times")