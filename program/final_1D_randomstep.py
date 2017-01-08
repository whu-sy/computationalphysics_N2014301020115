import random
import numpy as np
import pylab as pl

class one_dimension_walk:
    def __init__(self, num = 100, step_num = 100):
        self.step_num = np.arange(0, step_num + 1, 1)
        self.n = num
        self.x = [0]
        self.x2 = 0
        self.x2ave = [0]
    def run(self):
        for i in range(1, self.step_num[-1]+1):
            self.x2 = 0
            for j in range(self.n):
                self.x = [0]
                for k in range(i):
#                    temp = random.random()
                    if random.random() < 0.5:
                        self.x.append(self.x[-1] + random.random())
                    else:
                        self.x.append(self.x[-1] - random.random())
                self.x2 += self.x[-1]**2
            self.x2ave.append(self.x2 / self.n)
    def fit(self):
        self.z = np.polyfit(self.step_num, self.x2ave, 1)
    def show(self):
        pl.title('Random walk in one dimension', fontsize=20)
        pl.xlabel('step number', fontsize=20)
        pl.ylabel('x', fontsize=20)
        pl.plot(self.step_num, self.x, 'o')
        pl.plot([0,self.step_num[-1]], [0, 0], '--')
        pl.show()

        pl.title('Random walk in one dimension', fontsize=20)
        pl.xlabel('step number (= time)', fontsize=20)
        pl.ylabel('$\\leftangle x^2\\rightangle$', fontsize=20)
        pl.ylim(0, max(self.x2ave))
        pl.text(self.step_num[-1]*0.05,max(self.x2ave)*0.8,\
                '$\\leftangle x^2\\rightangle$ versus time\
                \nthe number of ensembles : %d'%self.n, fontsize=20)
        pl.text(self.step_num[-1]*0.4,max(self.x2ave)*0.1,\
                'fitted line:\n$\\leftangle x^2\\rightangle=%0.4f%s%0.4f$'%(self.z[0],'\ n+',self.z[1]), fontsize=20)
        pl.plot(self.step_num, self.x2ave, '.')
        pl.plot([0,self.step_num[-1]], [self.z[1], self.step_num[-1]*self.z[0]+self.z[1]], 'k')
        pl.show()
        
for i in [100,500,1000,5000]:
    start = one_dimension_walk(i)
    start.run()
    start.fit()
    start.show()
