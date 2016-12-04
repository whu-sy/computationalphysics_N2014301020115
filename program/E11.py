"""
P128 4.19
"""
import math
import matplotlib.pylab as pl

class Hyperion:
    def __init__(self, theta = 0, v = 2 * math.pi, total_time = 10, r = 1):
        self.C = 4 * math.pi**2 #GM_S
        self.e = 1 - r * v**2 / self.C
        self.x = [r]
        self.y = [0]
        self.vx = 0
        self.vy = v
        self.r = [r]
        self.omega = [0]
        self.theta = [theta]
        self.total_time = total_time
        self.dt = 0.0001
        self.t = [0]
    def calculate(self):
        while(self.t[-1] <= self.total_time):
            self.omega.append(self.omega[-1] - 3 * self.C / self.r[-1]**5
                              * (self.x[-1] * math.sin(self.theta[-1]) - self.y[-1] * math.cos(self.theta[-1]))
                              * (self.x[-1] * math.cos(self.theta[-1]) + self.y[-1] * math.sin(self.theta[-1])) * self.dt)
            self.theta.append(self.theta[-1] + self.omega[-1] * self.dt)
            if self.theta[-1] < -math.pi:
                self.theta[-1] = self.theta[-1] + 2 * math.pi
            if self.theta[-1] > math.pi:
                self.theta[-1] = self.theta[-1] - 2 * math.pi
            self.vx = self.vx - self.C * self.x[-1] * self.dt / self.r[-1]**3
            self.x.append(self.x[-1] + self.vx * self.dt)
            self.vy = self.vy - self.C * self.y[-1] * self.dt / self.r[-1]**3
            self.y.append(self.y[-1] + self.vy * self.dt)
            self.r.append(math.hypot(self.x[-1], self.y[-1]))
            self.t.append(self.t[-1] + self.dt)
    def show_result_theta(self):
        if self.e == 0:
            pl.title('Hyperion $\\theta$ versus time (Circular orbit)', fontsize=20)
        else:
            pl.title('Hyperion $\\theta$ versus time (Elliptical orbit)', fontsize=20)
        pl.xlabel('time(yr)', fontsize=20)
        pl.ylabel('$\\theta$(radians)', fontsize=20)
        pl.plot(self.t, self.theta)
        pl.xlim(0, self.total_time)
        pl.show()
    def show_result_omega(self):
        if self.e == 0:
            pl.title('Hyperion $\\omega$ versus time (Circular orbit)', fontsize=20)
        else:
            pl.title('Hyperion $\\omega$ versus time (Elliptical orbit)', fontsize=20)
        pl.xlabel('time(yr)', fontsize=20)
        pl.ylabel('$\\omega$(radians/yr)', fontsize=20)
        pl.plot(self.t, self.omega)
        pl.xlim(0, self.total_time)
        pl.show()
    def show_result_comparison(self, v = 2 * math.pi, t = 10):
        H_1 = Hyperion(0, v, t)
        H_1.calculate()
        H_2 = Hyperion(0.01, v, t)
        H_2.calculate()
        dtheta = []
        i = 0
        while(i < len(H_1.t)):
            dtheta.append(abs(H_1.theta[i] - H_2.theta[i]))
            i += 1
#        Y = []
#        lambda_Numerator = lambda_Denominator = 0
#        for i0 in range(len(dtheta)):
#            Y.append(math.log(dtheta[i0], 10))
#        X_mean = sum(H_1.t)/len(H_1.t)
#        Y_mean = sum(Y)/len(Y)
#        print(X_mean, Y_mean)
#        for i1 in range(len(Y)):
#            lambda_Numerator += (H_1.t[i1] * Y[i1] - len(Y) * X_mean * Y_mean)
#            lambda_Denominator += (H_1.t[i1]**2 - len(Y) * X_mean**2)
#        lambda0 = lambda_Numerator / lambda_Denominator
#        b0 = Y_mean - lambda0 * X_mean
#        print(lambda0, b0)
        if H_1.e == 0:
            pl.title('Hyperion $\\Delta\\theta$ versus time (Circular orbit)', fontsize=20)
        else:
            pl.title('Hyperion $\\Delta\\theta$ versus time (Elliptical orbit)', fontsize=20)
        pl.xlabel('time(yr)', fontsize=20)
        pl.ylabel('$\\Delta\\theta$(radians)', fontsize=20)
        pl.semilogy(H_1.t, dtheta)
        pl.plot([0, 0.7 * t], [dtheta[0] * 0.1, math.e**(00 * t * 0.7)], '--g')
        pl.xlim(0, H_1.total_time)
        pl.show()
        
        
        
#Hyperion(theta, v, total_time, r)
start = Hyperion(0, 5, 1)
#start.calculate()
#start.show_result_theta()
#start.show_result_omega()
start.show_result_comparison(5)