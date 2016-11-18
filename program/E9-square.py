"""
P88 3.30-3.32
"""
import math
import pylab as pl

class billiaro_collision_square:
    #初始化
    def __init__(self, x = 0, y = 0, vx = 1.13, vy = 1, total_time = 100):
        self.x = [x]
        self.y = [y]
        self.vx = vx
        self.vy = vy
        self.total_road = total_time * math.hypot(vx, vy)
        self.passed_road = [0]
        print("\n小球的横向与纵向的分速度分别为：", self.vx, self.vy)
        print("运动总时间为：", total_time)
        print("运动的总路程为：", self.total_road)       
    #计算部分
    def calculate(self):
        loop_calculate = True
        while(loop_calculate):
            #匀速直线运动部分（循环）
            while(True):
                #速度方向垂直于y轴时
                if self.vx == 0 and self.vy > 0:
                    self.x.append(self.x[-1])
                    self.y.append(1)
                    self.vy = -self.vy
                    break
                #速度方向垂直于y轴时
                if self.vx == 0 and self.vy < 0:
                    self.x.append(self.x[-1])
                    self.y.append(-1)
                    self.vy = -self.vy
                    break
                #速度方向在第一象限
                if self.vx > 0 and self.vy >= 0:
                    #以小球位置与墙壁拐角处连线把第一象限分成两部分，速度在逆时针方向的前一半
                    if self.vy / self.vx < (1 - self.y[-1]) / (1 - self.x[-1]):
                        self.y.append(self.vy / self.vx + self.y[-1] - self.x[-1] * self.vy / self.vx)
                        self.x.append(1)
                        self.vx = -self.vx
                        break
                    #以小球位置与墙壁拐角处连线把第一象限分成两部分，速度在逆时针方向的后一半
                    if self.vy / self.vx > (1 - self.y[-1]) / (1 - self.x[-1]):
                        self.x.append((1 - self.y[-1] + self.x[-1] * self.vy / self.vx) * self.vx / self.vy)
                        self.y.append(1)
                        self.vy = -self.vy
                        break
                    #速度与小球位置与墙壁拐角处连线的方向重合
                    if self.vy / self.vx == (1 - self.y[-1]) / (1 - self.x[-1]):
                        self.x.append(1)
                        self.y.append(1)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
                #速度方向在第二象限
                if self.vx < 0 and self.vy >= 0:
                    if self.vy / self.vx < (1 - self.y[-1]) / (-1 - self.x[-1]):
                        self.x.append((1 - self.y[-1] + self.x[-1] * self.vy / self.vx) * self.vx / self.vy)
                        self.y.append(1)
                        self.vy = -self.vy
                        break
                    if self.vy / self.vx > (1 - self.y[-1]) / (-1 - self.x[-1]):
                        self.y.append(-self.vy / self.vx + self.y[-1] - self.x[-1] * self.vy / self.vx)
                        self.x.append(-1)
                        self.vx = -self.vx
                        break
                    if self.vy / self.vx == (1 - self.y[-1]) / (-1 - self.x[-1]):
                        self.x.append(-1)
                        self.y.append(1)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
                #速度方向在第三象限
                if self.vx < 0 and self.vy <= 0:
                    if self.vy / self.vx < (-1 - self.y[-1]) / (-1 - self.x[-1]):
                        self.y.append(-self.vy / self.vx + self.y[-1] - self.x[-1] * self.vy / self.vx)
                        self.x.append(-1)
                        self.vx = -self.vx
                        break
                    if self.vy / self.vx > (-1 - self.y[-1]) / (-1 - self.x[-1]):
                        self.x.append((-1 - self.y[-1] + self.x[-1] * self.vy / self.vx) * self.vx / self.vy)
                        self.y.append(-1)
                        self.vy = -self.vy
                        break
                    if self.vy / self.vx == (-1 - self.y[-1]) / (-1 - self.x[-1]):
                        self.x.append(-1)
                        self.y.append(-1)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
                #速度方向在第四象限
                if self.vx > 0 and self.vy <= 0:
                    if self.vy / self.vx < (-1 - self.y[-1]) / (1 - self.x[-1]):
                        self.x.append((-1 - self.y[-1] + self.x[-1] * self.vy / self.vx) * self.vx / self.vy)
                        self.y.append(-1)
                        self.vy = -self.vy
                        break
                    if self.vy / self.vx > (-1 - self.y[-1]) / (1 - self.x[-1]):
                        self.y.append(self.vy / self.vx + self.y[-1] - self.x[-1] * self.vy / self.vx)
                        self.x.append(1)
                        self.vx = -self.vx
                        break
                    if self.vy / self.vx == (-1 - self.y[-1]) / (1 - self.x[-1]):
                        self.x.append(1)
                        self.y.append(-1)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
            #累计路程
            self.passed_road.append(self.passed_road[-1] + math.hypot(self.x[-1] - self.x[-2], self.y[-1] - self.y[-2]))
            #判断路程是不是超过了总路程
            if self.passed_road[-1] > self.total_road:
                temp_x = self.x[-1]
                temp_y = self.y[-1]
                #计算出小球的停止位置
                self.x[-1] = self.x[-2] + (temp_x - self.x[-2]) * (self.total_road - self.passed_road[-2]) / math.hypot(temp_x - self.x[-2], temp_y - self.y[-2])
                self.y[-1] = self.y[-2] + (temp_y - self.y[-2]) * (self.total_road - self.passed_road[-2]) / math.hypot(temp_x - self.x[-2], temp_y - self.y[-2])
                loop_calculate = False
            #经过的路程恰好等于总路程
            if self.passed_road[-1] == self.total_road:
                loop_calculate = False
    #画图
    def show_result(self):
        pl.title('Trajectory of a billiard on a square table')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.xlim(-1, 1)
        pl.ylim(-1, 1)
        pl.plot(self.x, self.y)
        pl.show()

num_str_in = input("请输入小球初始位置的横、纵坐标x、y，小球初始速度的横、纵分量vx、vy，运动持续时间t的值,并用空格隔开:\n")
num = [float(n) for n in num_str_in.split()]
x = num[0]
y = num[1]
vx = num[2]
vy = num[3]
total_time = num[4]
start = billiaro_collision_square(x, y, vx, vy, total_time)
start.calculate()
start.show_result()