#Y(x)=1/x*sin(5*x), x=[-5...5] (27 варіанту в списку немає, то я обрала 2)

from numpy import *
import matplotlib.pyplot as plt

x=linspace(-5,5)
y=1/x*sin(5*x)

plt.plot(x,y,'-c')
plt.title('Plot v2')
plt.savefig('Ex1.png', dpi=200)
plt.show()