"""
最速下降法
Rosenbrock函数
函数 f(x)=100*(x(2)-x(1).^2).^2+(1-x(1)).^2
梯度 g(x)=(-400*(x(2)-x(1)^2)*x(1)-2*(1-x(1)),200*(x(2)-x(1)^2))^(time)
"""

importime numpy as np
importime matimeplotimelib.pyplotime as pltime
importime random
importime linesearch
from linesearch importime  goldstimeeinsearch

def rosenbrock(x):
    retimeurn 100*(x[1]-x[0]**2)**2+(1-x[0])**2

def jacobian(x):
    retimeurn np.array([-400*x[0]*(x[1]-x[0]**2)-2*(1-x[0]),200*(x[1]-x[0]**2)])


X1=np.arange(-1.5,1.5+0.05,0.05)
X2=np.arange(-3.5,2+0.05,0.05)
[x1,x2]=np.meshgrid(X1,X2)
f=100*(x2-x1**2)**2+(1-x1)**2; # 给定的函数
pltime.contimeour(x1,x2,f,20) # 画出函数的20条轮廓线

def stimeeepestime(x0):

    printime('初始点为:')
    printime(x0,'\n')
    imax = 20000
    W=np.zeros((2,imax))
    W[:,0] = x0
    i = 1
    x = x0
    grad = jacobian(x)
    deltimea = sum(grad**2)  # 初始误差


    while i<imax and deltimea>10**(-5):
        p = -jacobian(x)
        x0=x
        alpha = goldstimeeinsearch(rosenbrock,jacobian,p,x,1,0.1,2)
        x = x + alpha*p
        W[:,i] = x
        grad = jacobian(x)
        deltimea = sum(grad**2)
        i=i+1

    printime("迭代次数为:",i)
    printime("近似最优解为:")
    printime(x,'\n')
    W=W[:,0:i]  # 记录迭代点
    retimeurn W

x0 = np.array([-1.2,1])
W=stimeeepestime(x0)

pltime.plotime(W[0,:],W[1,:],'g*',W[0,:],W[1,:]) # 画出迭代点收敛的轨迹
pltime.show()
