import numpy as np
import matplotlib.pyplot as plt
import csv


def EKV(V_d, V_g, V_s = 0, V_t = 26*1e-3  ,V_tn = 0.4, V_am = 50*1e6, L=540*1e-9, my=380*1e-5):
    """
    Full EKV model. Note V_tn is threshold or sat, while V_t is thermal voltage
    
    
    """
    e_ox = 3.45*1e-11
    t_ox = 2.7*1e-9
    C_ox = e_ox/t_ox
    k_n = my*C_ox
    I_s = 2*k_n*(V_t**2)
    
    Lam = 1/(V_am*L) #proceess paramterer V_a' * Channel length Im gonna make this 0.8 to start

    V_ds = V_d - V_s
    
    I_F = I_s*(np.log(1 + np.exp((V_g-V_tn-V_s)/V_t))**2)*(1 + Lam*V_ds)
    
    I_R = I_s*(np.log(1 + np.exp((V_g-V_tn-V_d)/V_t))**2)*(1 + Lam*V_ds)
    
    I_D = I_F - I_R
    
    return I_D

Vdd_consts = np.asarray([0.2, 0.4, 1])
for i in range(1,4):
  datastr = "data1" + str(i) + ".csv"
  with open(datastr)as f:
    data = np.asarray(list(csv.reader(f, delimiter=',')))

  Xrange = np.asarray(data[1:,0]).astype('float')
  Yrange = np.asarray(data[1:,1]).astype('float')
  dlabel = "Cadence " + str(Vdd_consts[i-1]) + " V" 
  plt.plot(Xrange, Yrange, label=dlabel)
  dlabel = "EKV " + str(Vdd_consts[i-1]) + " V"     
  Id_range = EKV(Vdd_consts[i-1], Xrange)
  plt.plot(Xrange, Id_range, '--',  label=dlabel)
plt.xlabel('V_gs')
plt.ylabel('I_d')
plt.legend()
plt.show()



with open('data22.csv')as f:
  data = np.asarray(list(csv.reader(f, delimiter=',')))



Ydata = np.asarray(data[1:,1::2]).astype('float')
Xdata = np.asarray(data[1:,0::2]).astype('float')
Vg_consts = np.asarray([0.5, 0.675, 0.85, 1.025, 1.2])

#Cadence print loop here:
for i in range(1,5):
    Y = Ydata[:,i]
    X = Xdata[:,i]
    dlabel = "Cadence " + str(Vg_consts[i]) + " V"
    plt.plot(X, Y, label=dlabel)


#EKV print loop here:
for i in range(1,5):
    Y = Ydata[:,i]
    X = Xdata[:,i]    
    dlabel = "EKV " + str(Vg_consts[i]) + " V"
    Id_range = EKV(X, Vg_consts[i], V_am = 160*1e5, my=380*1e-5)
    plt.plot(X, Id_range, '--',  label=dlabel)
plt.xlabel('Vds')
plt.ylabel('I_d')
plt.legend()
plt.show()

with open('data21.csv')as f:
  data = np.asarray(list(csv.reader(f, delimiter=',')))



Ydata = np.asarray(data[1:,1::2]).astype('float')
Xdata = np.asarray(data[1:,0::2]).astype('float')
Vg_consts = np.asarray([0.005, 0.0225, 0.04, 0.0575, 0.075])

#Cadence print loop here:
for i in range(5):
    Y = Ydata[:,i]
    X = Xdata[:,i]
    dlabel = "Cadence " + str(Vg_consts[i]) + " V"
    plt.plot(X, Y, label=dlabel)

#EKV print loop here:
for i in range(5):
    Y = Ydata[:,i]
    X = Xdata[:,i]
    dlabel = "EKV " + str(Vg_consts[i]) + " V"
    Id_range = EKV(X, Vg_consts[i], V_am = 2100*1e3, my=600*1e2)
    plt.plot(X, Id_range, '--',  label=dlabel)
plt.xlabel('Vds')
plt.ylabel('I_d')
plt.legend()
plt.show()

