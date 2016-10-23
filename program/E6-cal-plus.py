"""
P31 2.10 (include wind.迎面风阻)
"""
#import pylab as pl
import math

class cannon_shell:
    def __init__(self, init_v = 0, init_theta = 0, time_step = 0, target_altitude = 0, wind_speeed = 0):
        self.x = [0]
        self.y = [0]
        self.init_v = init_v
        self.init_theta = init_theta
        self.vx = [self.init_v * math.cos(self.init_theta / 180 * math.pi) / 1000]
        self.vy = [self.init_v * math.sin(self.init_theta / 180 * math.pi) / 1000]
        self.v_wind = wind_speeed / 1000
        self.dt = time_step
        self.C = 0
        self.h = target_altitude
    def launch(self):
        i = 0
        j = 0
        global high_enough
        global ts
        ts = True
        loop_launch = True
        while(loop_launch):
            if (1 - 6.5 * self.y[i] / 288.15) < 0:
                ts = False
                break
            self.C = 4E-2 * math.pow(1 - 6.5 * self.y[i] / 288.15, 2.5)
            self.x.append(self.x[i] + self.vx[i] * self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i] - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * abs(self.vx[i] - self.v_wind) * self.dt)
            self.vy.append(self.vy[i] - 9.8E-3 * self.dt - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * self.dt)
            i += 1
            if (self.y[i] < self.y[i-1]) and (self.y[i-1] < self.h):
                high_enough = False
                loop_launch = False
            if (self.y[i] > self.h) or j:
                j += 1
            if (self.y[i] < self.h) and j:
                loop_launch = False
        if self.y[i-1] > self.h:
            self.x[i] = -(self.y[i-1] - self.h) * (self.x[i] - self.x[i-1]) / (self.y[i] - self.y[i-1]) + self.x[i-1]
            self.y[i] = self.h
            high_enough = True

class shoot(cannon_shell):
    def find_maxrange(self):
        self.max_range = 0
        self.max_range_theta = self.theta_begin
        temp_max = 0
        loop_maxrange = True
        while(loop_maxrange):
            cannon_shell.__init__(self, self.v, self.max_range_theta, user_input.time_step, user_input.target_y, user_input.wind_speeed)
            cannon_shell.launch(self)
            temp_max = self.x[-1]
            if high_enough and ts:
                if self.max_range <= temp_max:
                    self.max_range = temp_max
                    self.max_range_theta += self.theta_step
                else:
                    self.max_range_theta -= self.theta_step
                    loop_maxrange = False
            else:
                self.max_range_theta += self.theta_step
            if self.max_range_theta > self.theta_stop:
                loop_maxrange = False
    def detal(self):
        if self.C == 0:
            self.v_step = 10
            self.theta_step = 1
            self.v_begin = 0
            self.v_stop = 1000
            self.theta_begin = 0
            self.theta_stop = 90
            print("第一层循环需要的时间比较多，请耐心等待。。。\n\n", [self.v_begin, self.v_stop, self.v_step], [self.theta_begin, self.theta_stop, self.theta_step], "\n")
        else:
            self.v_begin = self.temp_v - self.v_step
            self.v_stop = self.temp_v + self.v_step
            self.theta_begin = self.temp_theta - self.theta_step
            self.theta_stop = self.temp_theta + self.theta_step
            self.v_step = self.v_step / 10
            self.theta_step = self.theta_step / 10
            print([self.v_begin, self.v_stop, self.v_step], [self.theta_begin, self.theta_stop, self.theta_step], "\n")
    def find_close_v(self):
        self.temp_v = 0
        self.temp_theta = 0
        self.d = 0
        self.v = self.v_begin
        loop_v = True
        while(loop_v):
            shoot.find_maxrange(self)
            if high_enough and self.max_range >= user_input.target_x:
                self.temp_v = self.v
                self.temp_theta = self.max_range_theta
                self.d = self.max_range - user_input.target_x
                loop_v = False
            self.v += self.v_step
            if self.v > self.v_stop:
                loop_v = False
    def find(self):
        temp_loop_level = 0
        loop_find = True
        print("expected loop_level:", user_input.loop_level, "\n--------------\n")
        while(loop_find):
            shoot.detal(self)
            shoot.find_close_v(self)
            print(self.temp_v)
            print(self.temp_theta)
            print(self.d)
            temp_loop_level +=1
            print("loop_level = ", temp_loop_level, "\n--------------\n")
            if temp_loop_level >= user_input.loop_level:
                loop_find = False
        print(self.temp_v)
        print(self.temp_theta)
        print(self.d)

class user_input:
    num_str_in = input("请输计算间隔dt（s）的值,横向风速（m/s）,靶点横向距离（km）,靶点高度（km）,计算层数,并用空格隔开:\n")
    num = [float(n) for n in num_str_in.split()]
    init_v = 0
    init_theta = 0
    
    time_step = num[0]
    wind_speeed = num[1]
    target_x = num[2]
    target_y = num[3]
    loop_level = num[4]

#运行程序
user_input()

start = shoot(user_input.init_v, user_input.init_theta, user_input.time_step, user_input.target_y, user_input.wind_speeed)
start.find()
end = input("\n\n\n按下回车结束程序...")