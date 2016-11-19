"""
P88 3.30-3.32
"""
import math
import pylab as pl
import matplotlib.patches as pt

class billiaro_collision_circle:
    #初始化
    def __init__(self, x = 0.2, y = 0, vx = 1.7, vy = 1, total_time = 1000):
        self.x = [x]
        self.y = [y]
        self.vx = vx
        self.vy = vy
        self.v = [vx, vy]
        self.ps_x = []
        self.ps_vx = []
        self.total_road = total_time * math.hypot(vx, vy)
        self.passed_road = [0]
        self.kr = 0
        print("\n小球的横向与纵向的分速度分别为：", self.vx, self.vy)
        print("运动总时间为：", total_time)
        print("运动的总路程为：", self.total_road)
    #向量的数量积(tne vector dot product)
    def vdp(a, b):
        return(a[0] * b[0] + a[1] * b[1])
#    #向量的和
#    def vadd(a, b):
#        return([a[0] + b[0], a[1] + b[1]])
    #向量的差
    def vsub(a, b):
        return([a[0] - b[0], a[1] - b[1]])
    #向量的数乘(multiplication of vector by scalar)
    def vsm(a, b):
        return([a * b[0], a * b[1]])
    #法向量
    def n_cal(self):
        if self.x[-1] > 0:
            if self.y[-1] > 0:
                return([-1 / math.sqrt(self.kr**2 + 1), -self.kr / math.sqrt(self.kr**2 + 1)])
            else:
                return([-1 / math.sqrt(self.kr**2 + 1), -self.kr / math.sqrt(self.kr**2 + 1)])
        else:
            if self.y[-1] > 0:
                return([1 / math.sqrt(self.kr**2 + 1), self.kr / math.sqrt(self.kr**2 + 1)])
            else:
                return([1 / math.sqrt(self.kr**2 + 1), self.kr / math.sqrt(self.kr**2 + 1)])
    #计算部分
    def calculate(self):
        loop_calculate = True
        while(loop_calculate):#并没有考虑速度垂直于x轴的情况
            k = self.v[1] / self.v[0]
            b = self.y[-1] - self.x[-1] * k
            temp_vx = self.v[0]
            #匀速直线运动部分（循环）
            while(True):
                #速度的横向分量大于零时
                if self.v[0] > 0:
                    self.x.append((-k * b + math.sqrt(k**2 - b**2 + 1)) / (k**2 + 1))
                    self.y.append((b + k * math.sqrt(k**2 - b**2 + 1)) / (k**2 + 1))
                    break
                #速度的横向分量小于零时
                if self.v[0] < 0:
                    self.x.append((-k * b - math.sqrt(k**2 - b**2 + 1)) / (k**2 + 1))
                    self.y.append((b - k * math.sqrt(k**2 - b**2 + 1)) / (k**2 + 1))
                    break
            #求反弹后的速度
            self.kr = self.y[-1] / self.x[-1]
            n = billiaro_collision_circle.n_cal(self)
            self.v = billiaro_collision_circle.vsub(self.v, billiaro_collision_circle.vsm(2 * billiaro_collision_circle.vdp(self.v, n),  n))
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
            #记录Poincare section的数据
            if self.y[-1] * self.y[-2] < 0:
                self.ps_vx.append(temp_vx)
                self.ps_x.append(self.x[-2] + (self.x[-1] - self.x[-2]) * (0 - self.y[-2]) / (self.y[-1] - self.y[-2]))
    #画碰撞轨迹图
    def show_result(self):
        fig = pl.figure()
        pl.title('Trajectory of a billiard on a square table', fontsize=20)
        pl.xlabel('x', fontsize=20)
        pl.ylabel('y', fontsize=20)
        ax = fig.add_subplot(111)
        cir1 = pt.Circle(xy = (0, 0), radius=1, alpha=1, fill = False)#第一个参数为圆心坐标,第二个为半径,第三个为透明度(0-1)
        ax.add_patch(cir1)
        pl.xlim(-1, 1)
        pl.ylim(-1, 1)
        pl.plot(self.x, self.y)
        pl.show()
    #画Poincare section图
    def show_result_ps(self):
        pl.title('Poincare section $v_x$ versus x', fontsize=20)
        pl.xlabel('x', fontsize=20)
        pl.ylabel('$v_x$', fontsize=20)
        pl.xlim(-1, 1)
        pl.ylim(-math.hypot(self.vx, self.vy), math.hypot(self.vx, self.vy))
        pl.plot(self.ps_x, self.ps_vx, '.')
        pl.show()

num_str_in = input("请输入小球初始位置的横、纵坐标x、y，小球初始速度的横、纵分量vx、vy，运动持续时间t的值,并用空格隔开:\n")
num = [float(n) for n in num_str_in.split()]
x = num[0]
y = num[1]
vx = num[2]
vy = num[3]
total_time = num[4]
start = billiaro_collision_circle(x, y, vx, vy, total_time)
start.calculate()
start.show_result()
start.show_result_ps()

#start = billiaro_collision_circle()
#start.calculate()
#start.show_result()
#start.show_result_ps()