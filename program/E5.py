"""
P31 2.9
"""
import pylab as pl
import math

class cannon_shell:
    def __init__(self, init_v, init_theta, time_step):
        self.x = [0]
        self.y = [0]
        self.init_theta = init_theta
        self.vx = [init_v * math.cos(self.init_theta / 180 * math.pi) / 1000]
        self.vy = [init_v * math.sin(self.init_theta / 180 * math.pi) / 1000]
        self.dt = time_step
        self.C = 0
        self.g = 9.8E-3
    def launch(self):
        i = 0
        while(True):
            self.C = 4E-2 * math.pow(1 - 6.5 * self.y[i] / 288.15, 2.5)
            self.x.append(self.x[i] + self.vx[i] * self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i] - self.C * math.hypot(self.vx[i], self.vy[i]) * self.vx[i] * self.dt)
            self.vy.append(self.vy[i] - self.g * self.dt - self.C * math.hypot(self.vx[i], self.vy[i]) * self.vy[i] * self.dt)
            i += 1
            if self.y[i] < 0:
                break
        self.x[i] = -self.y[i-1] * (self.x[i] - self.x[i-1]) / (self.y[i] - self.y[i-1]) + self.x[i-1]
        self.y[i] = 0

class maximum_range(cannon_shell):
    def find(self):
        max_range = 0
        temp_max = 0
        init_theta = 0
        print("\n此初速度下最大落地距离的计算过程预计需几十秒，请耐心等待...\n")
        while(True):
            cannon_shell.__init__(self, init_v, init_theta, time_step)
            cannon_shell.launch(self)
            temp_max = self.x[-1]
            if (max_range <= temp_max):
                max_range = temp_max
                init_theta += 0.1
            else:
                init_theta -= 0.1
                break
        print("在此初速度下落地最大距离为: %.4f km"%max_range)
        print("此时的发射角为: %.1f °"%init_theta)

def show_results(self):
    print("初速度：", init_v, "m/s")
    print("发射角度：", init_theta, "°")
    print("计算间隔：", time_step, "s")
    print("落地距离：%.4f km"%self.x[-1])
    pl.plot(self.x, self.y)
    pl.title('Cannon Shell')
    pl.xlabel('x / $km$')
    pl.ylabel('y / $km$')
    pl.grid()
    pl.show()

num_str_in = input("请输入初速度（m/s),初始角度（角度），dt（s）的值,并用空格隔开:\n")
num = [float(n) for n in num_str_in.split()]
init_v = num[0]
init_theta = num[1]
time_step = num[2]
start = cannon_shell(init_v, init_theta, time_step)
start.launch()
show_results(start)

start = maximum_range(init_v, init_theta, time_step)
start.find()
end = input("\n按下回车结束程序...")