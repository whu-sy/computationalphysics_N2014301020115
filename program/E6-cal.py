"""
P31 2.10 (include wind.迎面风阻)
"""
import math

#计算轨迹
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
        global ts
        ts = 0
        loop = True
        global high_enough
        while(loop):
            if (1 - 6.5 * self.y[i] / 288.15) < 0:
                break
            else:
                ts = 1
            self.C = 4E-2 * math.pow(1 - 6.5 * self.y[i] / 288.15, 2.5)
            self.x.append(self.x[i] + self.vx[i] * self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i] - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * abs(self.vx[i] - self.v_wind) * self.dt)
            self.vy.append(self.vy[i] - 9.8E-3 * self.dt - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * self.dt)
            i += 1
            if (self.y[i] < self.y[i-1]) and (self.y[i-1] < self.h):
                high_enough = False
                loop = False
            if (self.y[i] > self.h) or j:
                j += 1
            if (self.y[i] < self.h) and j:
                loop = False
        if self.y[i-1] > self.h:
            self.x[i] = -(self.y[i-1] - self.h) * (self.x[i] - self.x[i-1]) / (self.y[i] - self.y[i-1]) + self.x[i-1]
            self.y[i] = self.h
            high_enough = True

#计算最小出射速度并输出
class shoot(cannon_shell):
    def find(self):
        print("\n正在计算，请稍后...\n")
        self.min_v = 1000000
        self.min_theta = 0
        self.d = 1000
        loop_theta = True
        loop_v = True
        init_v = 0
        while(loop_v):
            init_theta = 0
            loop_theta = True
            while(loop_theta):
                shoot.__init__(self, init_v, init_theta, user_input.time_step, user_input.target_altitude, user_input.wind_speeed)
                shoot.launch(self)
                temp_d = abs(self.x[-1] - user_input.target_x)
                if high_enough and ts:
                    if self.d >= temp_d:
                        self.d = temp_d
                        self.min_theta = init_theta
                init_theta += 1
                if init_theta >= 90:
                    loop_theta = False
            if self.d < 0.01:
                self.min_v = init_v
                loop_v = False
            init_v += 10
    def show_result(self):
        print("最小出射速度为：", self.min_v, "m/s\n")
        print("此时的出射角为：", self.min_theta, "°\n")
        print("此时落点与靶之间的误差距离为：%.4f m："%(self.d * 1000))

#用户输入初值
class user_input:
    num_str_in = input("请输入计算间隔dt（s）的值,风速（m/s）,靶点距发射点距离（km）,靶点高度（km）并用空格隔开:\n")
    num = [float(n) for n in num_str_in.split()]
    time_step = num[0]
    wind_speeed = num[1]
    target_altitude = num[2]
    target_x = num[3]
    target_y = target_altitude
    init_v = 1000
    init_theta = 0

#运行程序
user_input()
start = shoot(user_input.init_v, user_input.init_theta, user_input.time_step, user_input.target_altitude, user_input.wind_speeed)
start.find()
start.show_result()
end = input("\n\n\n按下回车结束程序...")