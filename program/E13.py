import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation

delta_x, c ,r , k = 0.001, 300 , 1 , 1000
delta_t=delta_x/c
T=0.04
N=int(T*c/delta_x)
t=np.linspace(0,T,N+1)

def next_step(y_previous,y_current):
    y_next=[0]
    c1,c2=2*(1-r**2),r**2
    for i in range(1,len(y_current)-1):
        y_next.append(c1*y_current[i]-y_previous[i]+c2*(y_current[i-1]+y_current[i+1]))
    y_next.append(0)
    return y_next

def initial_Gaussian(x_excite):#initialize or excite the string in some point in the gaussian way
    y_initial=[]           
    for i in range(1+int(1./delta_x)):
        y_initial.append(math.exp(-k*(i*delta_x-x_excite)**2))
    return y_initial

def initial_real(x_excite):#initialize or excite the string in some point in the real way
    y_initial=[]
    for i in range(int(x_excite/delta_x)):
        y_initial.append(i*delta_x/x_excite)
    for i in range(int(x_excite/delta_x),1+int(1./delta_x)):
        y_initial.append((i*delta_x-1.)/(x_excite-1))
    return y_initial

def motion_of_a_point(x_observe,x_excite):
    y_initial=initial_real(x_excite) #this can be changed accrodingly
    y_observe=[]                  #calculate the displacement at x=0.05 or y(i=I,n)
    I=int(x_observe/delta_x)
    y0=y_initial
    y1=y_initial
    y_observe.append(y1[I])
    for i in range(N):
        y2=next_step(y0,y1)
        y0,y1=y1,y2
        y_observe.append(y1[I])
    return y_observe


#plot
x_observe_list,x_ex=[0.05,0.1,0.2,0.3],0.45

for i in range(4):
    x_ob=x_observe_list[i]
    yx=motion_of_a_point(x_ob,x_ex)
    ps=abs(np.fft.rfft(yx))**2
    freq= np.linspace(0, c/delta_x/2, len(ps))
    
    plt.subplot(1,2,1)
    plt.plot(t,yx)
    plt.title('String Signal versus Time')
    plt.xlabel('time(s)')
    plt.ylabel('Signal(arbitrary units)')
    #plt.text(0.,0.4,r'R Wavepacket,$y_0(x)=exp[-1000\times(x-%s)^2]$'%x_ex+'\n$x_{observe}=%s$'%x_ob)
    plt.text(0.1,0.12,'Real Wavepacket of Two Straight Lines')
    plt.xlim(0,T)
    
    plt.subplot(1,2,2)
    plt.plot(freq,ps)
    plt.xlim(0,3000)
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Power')
    plt.title('Power spectrum')
    #plt.text(1500,200000,r'Gaussian Wavepacket'+'\n$y_0(x)=exp[-1000*(x-%s)^2]$'%x_ex+'\n$x_{observe}=%s$'%x_ob)
    plt.text(1500,200000,r'Real Wavepacket'+'\n$x_{excite}=$%s'%x_ex+'\n$x_{observe}=%s$'%x_ob)
    
    plt.show()