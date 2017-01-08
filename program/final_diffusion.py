#二维扩散
import random
import matplotlib.pyplot as plt

class diffusion:
    def __init__(self, t = 2, n = 1, long = 100):
        self.t=t
        self.n=n
        self.long=long
        self.y=[]
        self.a=[]
        self.b=[]
    def cal(self):
        for i in range(self.long):
            if i<=7*self.long/16 or i>=9*self.long/16:
               self.b.append(0)
            else:
               self.b.append(self.n)
        c=[0]*self.long
        for j in range(self.long):
            self.y.append(c[:])
            if j<=7*self.long/16 or j>=9*self.long/16:
               self.a.append(c[:])
            else:
               self.a.append(self.b[:])
        for j in range(self.t):
            for q in range(len(self.a)):
                for u in range(len(self.a)):
                    if self.a[q][u]!=0:
                       for i in range(self.a[q][u]):
                           cc=random.random()
                           self.a[q][u]=self.a[q][u]-1
                           if cc<=0.25:
                              if u+1<=len(self.a)-1:
                                 self.a[q][u+1]=self.a[q][u+1]+1
                           elif cc<=0.5:
                              if u-1>=0:
                                 self.a[q][u-1]=self.a[q][u-1]+1
                           elif cc<=0.75:
                              if q-1>=0:
                                 self.a[q-1][u]=self.a[q-1][u]+1
                           else:
                              if q+1<=len(self.a)-1:
                                 self.a[q+1][u]=self.a[q+1][u]+1                           
    def show(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                if self.a[i][j]!=0:
                   plt.scatter([i,],[j,],7,color='blue')
        plt.xlim(0,self.long)
        plt.ylim(0,self.long)
        plt.title('Diffusion (t=%d)'%self.t, fontsize=20)
        plt.xlabel('x', fontsize=20)
        plt.ylabel('y', fontsize=20)
        plt.show()

for i in [0, 10, 50, 100, 500]:
    start = diffusion(i)
    start.cal()
    start.show()