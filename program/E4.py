"""
P16 1.5
"""
import numpy as np
import pylab as pl

class transform:
    def __init__(self, na, nb, time_constant, time_of_duration, time_step = 0.05,):
        # unit of time is second
        self.na = [na]
        self.nb = [nb]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.total_time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.init_na = na
        self.init_nb = nb
        print("Initial number of A nuclei ->", na)
        print("Initial number of B nuclei ->", nb)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmpna = self.na[i] + (self.init_na + self.init_nb - 2 * self.na[i]) / self.tau * self.dt
            tmpnb = self.nb[i] + (self.init_na + self.init_nb - 2 * self.nb[i]) / self.tau * self.dt
            self.na.append(tmpna)
            self.nb.append(tmpnb)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.na, 'b', label = "$N_{A}$")
        pl.plot(self.t, self.nb, 'r', label = "$N_{B}$")
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        x = np.linspace(0, self.total_time, self.nsteps)  
        na_analytic = ((self.init_na + self.init_nb) + (self.init_na - self.init_nb) * np.exp(-2 / self.tau * x)) / 2
        nb_analytic = ((self.init_na + self.init_nb) - (self.init_na - self.init_nb) * np.exp(-2 / self.tau * x)) / 2
        pl.plot(x, na_analytic, 'b--', label = "theoretical value of $N_{A}$")
        pl.plot(x, nb_analytic, 'r--', label = "theoretical value of $N_{B}$")
        pl.legend()
        pl.grid()
        pl.show()
    def store_results(self):
        datafile = open('E4_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.na[i], self.nb[i], file = datafile)
        datafile.close()

num_str_in = input("请输入NA,NB,tau,模拟持续时间,dt的值,并用空格隔开:\n")
num = [float(n) for n in num_str_in.split()]
na = num[0]
nb = num[1]
time_constant = num[2]
time_of_duration = num[3]
time_step = num[4]
start = transform(na, nb, time_constant, time_of_duration, time_step)
start.calculate()
start.show_results()
start.store_results()