"""
P143 5.6
"""
import numpy as np
import matplotlib.pylab as pl
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

class Fields:
    #初始化参数：a：半边长, p：上平面电势, dx：步长
    def __init__(self, a = 1, p = 1, dx = 0.1):
        self.a = a
        self.dx = dx
        self.p = p
        self.l = int(2*a/dx+1)
        #避雷针位置
        self.rod_location = int(a/dx)
        #避雷针长度
        self.rod_len = int(self.l*0.75)
        #左右边界条件
        p0 = np.arange(0, self.p + self.p/(self.l-1), self.p/(self.l-1))
        #初始化电势矩阵
        self.V = np.array([[0.0 for i in range(self.l)]for j in range(self.l)])
        #加入初始条件
        for i in range(self.l):
            self.V[i, 0] = p0[i]
            self.V[i, self.l-1] = p0[i]
        for i in range(self.l):
            self.V[self.l-1, i] = self.p
        for i in range(self.rod_len):
            self.V[i, self.rod_location] = 0
    def calculate(self):
        loop = True
        while(loop):
            temp = self.V[7, 7]
            for i in range(1, self.l-1):
                for j in range(1, self.l-1):
                    self.V[i, j] = (self.V[i + 1, j] + self.V[i - 1, j] + self.V[i, j + 1] + self.V[i, j - 1]) / 4
                    for l in range(self.rod_len):
                        self.V[l, self.rod_location] = 0
            if temp == self.V[7, 7]:
                loop = False
    def show_result(self):
        X = np.arange(-self.a, self.a + self.dx, self.dx)
        Y = np.arange(-self.a, self.a + self.dx, self.dx)
        self.X, self.Y = np.meshgrid(X, Y)
        #等势线图
        pl.figure(figsize=[7,7])
        ct = pl.contour(self.X, self.Y, self.V,20)
        pl.clabel(ct, inline=1, fontsize=10)
        pl.xlim(-self.a,self.a)
        pl.xlabel('x', fontsize=20)
        pl.ylim(-self.a,self.a)
        pl.ylabel('y', fontsize=20)
        pl.title('Contours of Electric Potential', fontsize=20)
        pl.show()
        #3D透视图
        fig = pl.figure()
        ax = fig.gca(projection= '3d')
        surf = ax.plot_surface(self.X, self.Y, self.V, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax.set_xlim(-self.a, self.a)
        ax.set_ylim(-self.a, self.a)
        ax.set_zlim(0, self.p)
        ax.set_xlabel('X', fontsize=20)
        ax.set_ylabel('Y', fontsize=20)
        ax.set_zlabel('V', fontsize=20)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        ax.set_title("Perspective Plot of The Potential", fontsize=20)
        pl.show()
        #电场图
        V=np.array(self.V)
        Ex=np.array(self.V)
        Ey=np.array(self.V)
        for i in range(1,len(self.V)-1):
            for j in range(1,len(self.V)-1):
                Ex[i,j]=-(V[i,j+1]-V[i,j-1])/(2*self.dx)
                Ey[i,j]=-(V[i+1,j]-V[i-1,j])/(2*self.dx)
        pl.figure(figsize=[7,7])
        pl.quiver(X,Y,Ex,Ey,scale=100)
        pl.xlim(-self.a,self.a)
        pl.xlabel('x', fontsize=20)
        pl.ylim(-self.a,self.a)
        pl.ylabel('y', fontsize=20)
        pl.title('Electric Field', fontsize=20)
        pl.show()

start = Fields()
start.calculate()
start.show_result()
