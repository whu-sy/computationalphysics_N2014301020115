import math
import pylab as pl
#初始化各个值，以及计算单摆的运功轨迹，展示结果曲线图像
class pendulums_basis:
    def __init__(self, F_D = 1.2, total_time = 60, init_theta = 0.2, q = 0.5, l = 9.8, g = 9.8, Omega_D = 2/3, time_step = 0.04):
        self.omega = [0]
        self.theta = [init_theta]
        self.t = [0]
        self.dt = time_step
        self.total_time = total_time
        self.q = q
        self.l = l
        self.g = g
        self.Omega_D = Omega_D
        self.F_D = F_D
    def calculate(self):
        i = 0
        loop_calculate = True
        while(loop_calculate):
            self.omega.append(self.omega[i] + ((-self.g / self.l) * math.sin(self.theta[i]) - self.q * self.omega[i] + self.F_D * math.sin(self.Omega_D * self.t[i])) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            self.t.append(self.t[i] + self.dt)
            if self.theta[i + 1] < -math.pi:
                self.theta[i + 1] = self.theta[i + 1] + 2 * math.pi
            if self.theta[i + 1] > math.pi:
                self.theta[i + 1] = self.theta[i + 1] - 2 * math.pi
            i += 1
            if self.t[i] > self.total_time:
                loop_calculate = False
    def show_results(self):
        pl.plot(self.t, self.theta)
        pl.title("$\\theta$ versus $t$   $F_D=%.1f$"%self.F_D, fontsize=20)
        pl.xlabel('time(s)', fontsize=20)
        pl.ylabel('$\\theta$(radians)', fontsize=20)
        pl.show()
#计算两个几乎相同的摆，只是初始的$\theta$有微小的差异，每个时间点对应的$\Delta t=|\theta_1-\theta_2|$与时间$t$的关系曲线
class pendulums_comparison(pendulums_basis):
    def compare(self):
        pendulum_1 = pendulums_comparison(self.F_D, self.total_time, self.theta[0], 0.5)
        pendulum_1.calculate()
        pendulum_2 = pendulums_comparison(self.F_D, self.total_time, self.theta[0], 0.501)
        pendulum_2.calculate()
        dtheta = []
        loop_compare = True
        i = 0
        while(loop_compare):
            dtheta.append(abs(pendulum_1.theta[i] - pendulum_2.theta[i]))
            i += 1
            if i == len(pendulum_1.t):
                loop_compare = False
        pl.semilogy(pendulum_1.t, dtheta)
        pl.title("$\\Delta\\theta$ versus $t$   $F_D=%.1f$"%self.F_D, fontsize=20)
        pl.xlabel('time(s)', fontsize=20)
        pl.ylabel('$\\Delta\\theta$(radians)', fontsize=20)
        pl.show()
#展示$\omega$与$\theta$的关系曲线
class omega_versus_theta(pendulums_basis):
    def show_results(self):
        pl.plot(self.theta, self.omega, '.',)
        pl.title("$\\omega$ versus $\\theta$   $F_D=%.1f$"%self.F_D, fontsize=20)
        pl.xlabel('$\\theta$(radians)', fontsize=20)
        pl.ylabel('$\\omega$(radians/s)', fontsize=20)
        pl.show()
#展示在满足一定相位条件的$t$下$\omega$与$\theta$的关系曲线
class poincare_section(pendulums_basis):
    def calculate(self):
        i = 0
        n = 1
        self.ps_omega = []
        self.ps_theta = []
        loop_calculate = True
        while(loop_calculate):
            self.omega.append(self.omega[i] + ((-self.g / self.l) * math.sin(self.theta[i]) - self.q * self.omega[i] + self.F_D * math.sin(self.Omega_D * self.t[i])) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            self.t.append(self.t[i] + self.dt)
            if self.theta[i + 1] < -math.pi:
                self.theta[i + 1] = self.theta[i + 1] + 2 * math.pi
            if self.theta[i + 1] > math.pi:
                self.theta[i + 1] = self.theta[i + 1] - 2 * math.pi
            #$\Omega_Dt=2n\pi$
            if  abs(self.t[i + 1] - 2 * n * math.pi / self.Omega_D) < self.dt / 2:
                self.ps_omega.append(self.omega[-1])
                self.ps_theta.append(self.theta[-1])
                n += 1
#            #$\Omega_Dt=n\pi-\pi/2$
#            if  abs(self.t[i + 1] - (n * math.pi - 0.5 * math.pi) / self.Omega_D) < self.dt / 2:
#                self.ps_omega.append(self.omega[-1])
#                self.ps_theta.append(self.theta[-1])
#                n += 1
#            #$\Omega_Dt=2n\pi+\pi/4$
#            if  abs(self.t[i + 1] - (2 * n * math.pi + math.pi / 4) / self.Omega_D) < self.dt / 2:
#                self.ps_omega.append(self.omega[-1])
#                self.ps_theta.append(self.theta[-1])
#                n += 1
            i += 1
            if self.t[i] > self.total_time:
                loop_calculate = False
    def show_results(self):
        pl.plot(self.ps_theta, self.ps_omega, '.')
        pl.xlabel('$\\theta$(radians)', fontsize=20)
        pl.ylabel('$\\omega$(radians/s)', fontsize=20)
        pl.title('$\\omega$ versus $\\theta$ $F_D=1.2$', fontsize=20)
        pl.show()
#按需求运行程序
start_1 = pendulums_basis(0, 60)
start_1.calculate()
start_1.show_results()
start_2 = pendulums_basis(0.5, 60)
start_2.calculate()
start_2.show_results()
start_3 = pendulums_basis(1.2, 60)
start_3.calculate()
start_3.show_results()
#start_comparison_1 = pendulums_comparison(0.5, 50)
#start_comparison_1.compare()
#start_comparison_2 = pendulums_comparison(1.2, 50)
#start_comparison_2.compare()
#start_ovt_1 = omega_versus_theta(0.5, 40)
#start_ovt_1.calculate()
#start_ovt_1.show_results()
#start_ovt_2 = omega_versus_theta(1.2, 200)
#start_ovt_2.calculate()
#start_ovt_2.show_results()
#start_ps = poincare_section(1.2, 7000)
#start_ps.calculate()
#start_ps.show_results()