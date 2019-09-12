from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate

from scipy.integrate import fixed_quad
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from scipy.special import roots_legendre as leg

mark = 'a1'

rootNum = 10                    # Gaussian Quadrature 积分时取的根的个
                                # 数.
beta = 1                        # 温度的倒数.
zero = 1e-6                     # 积分从零开始时, 为避免发散, 从一个非
                                # 常小的数值开始积.
R = 1/30                        # 参数 k_epsilon R 的取值.
epsabs = 1e-1                   # 用 integrate.quad 积分时限定的绝对误
                                # 差 .

def printParamaters():
    print('Root number of Gaussian Quadrature is rootNUm =', rootNum)
    print('Temperature is beta =', beta)
    print('Paramater k_epsilon R =', rootNum)
    print('Small number zero =', zero)
    print('Absolute error epsabs =', epsabs)
    return None
printParamaters()
#定义用到的函数.
def xi(k, mu):
    return k**2 - mu
def n(k, mu):
    x = xi(k,mu)
    n =  1 / (np.exp(beta*x) - 1)
    return n
def z(omega, q, mu):
    return omega - q**2/2 + 2*mu
def pi(omega, q, k, mu):
    """没有积分时的 PI"""
    pi = 1 + n(k+q/2, mu) + n(-k+q/2, mu)
    pi = pi / (2*k**2 - z(omega, q, mu))
    pi = pi * k**4
    pi = pi -k**2/2 - z(omega, q, mu)/4
    pi = 2*pi / np.pi**2 * R
    return pi
def PI(omega, q, mu):
    """将函数 pi 中的 k 积分掉"""
    zz = z(omega, q, mu)
    if zz<0:
        PI, err = fixed_quad(lambda x: pi(omega, q, x, mu), zero, 10,
                             n=rootNum)
        # 积分范围是 [0, inf], 如果 z<0 , 在积分范围内分母没有零点, 直
        # 接积分即可.
    else:
        # 如果在积分范围内出现了零点, 就需要考虑它的主值积分.
        # 可以求得在积分范围内的零点为:
        a = np.sqrt(zz/2)
        # 在零点两侧分别积分, 然后相加.
        PI1, err = fixed_quad(lambda x: pi(omega, q, x, mu), zero, a-zero,
                              n=rootNum) 
        PI2, err = fixed_quad(lambda x: pi(omega, q, x, mu), a+zero,
                              10, n=rootNum)
        PI = PI1 + PI2
    return PI
def delta(omega, q, rkv, mu):
    """函数 delta^p"""
    zz = z(omega, q, mu)
    if zz<0:
        # 如果 z<0 , 它是没有虚部的.
        img = 0
    else:
        # 否则, 主值积分后会有一个虚部, 解析表达式为.
        k = np.sqrt(zz/2)
        img = 1 + n(k+q/2, mu) + n(-k+q/2, mu)
        img = img * R/(2*np.pi)
        img = img * k**3
    # delta 实部就是 PI 的实部再加上两项.
    rel = PI(omega, q, mu)
    rel = rel + rkv/(4*np.pi)
    rel = rel +zz/(4*np.pi)
    # delta 取其辐角. 为了使最后的积分收敛, 整体做一个 pi 相位的调整.
    delta = np.angle(rel + 1j*img) - np.pi
    return delta
def anaDelta(omega, q, rkv, mu):
    a = q**2/2 - 2*mu - rkv
    if omega<a:
        anaDelta = 0
    else:
        anaDelta = -np.pi
    return anaDelta

'''
Nrkv = 100
rkv = np.linspace(0, 2, Nrkv)
np.savetxt('rkv.txt', rkv)

Nmu = 10
mu = np.linspace(-2.1, -1.2, Nmu)
'''
def f(omega, q, rkv, mu):
    f = 1 / (np.exp(beta*omega) - 1)
    f = 3*f / np.pi
    f = f * delta(omega, q, rkv, mu)
    return f
def FF(q, rkv, mu):
    """把 omega 积掉."""
    FF, err = integrate.quad(lambda x:f(x, q, rkv, mu), -1.1, 3, epsabs=epsabs)
    return FF
def F(rkv, mu):
    """把 q 也积掉."""
    F, err = integrate.quad(lambda x:x**2*FF(x,rkv, mu), zero, 3, epsabs=epsabs)
    return F

def anaf(omega, q, rkv, mu):
    f = 1 / (np.exp(beta*omega) - 1)
    f = 3*f / np.pi
    f = f * anaDelta(omega, q, rkv, mu)
    return f
def anaFF(q, rkv, mu):
    """把 omega 积掉."""
    FF, err = integrate.quad(lambda x:anaf(x, q, rkv, mu), -1.1, 3, epsabs=epsabs)
    return FF
def anaF(rkv, mu):
    """把 q 也积掉."""
    F, err = integrate.quad(lambda x:x**2*anaFF(x,rkv, mu), zero, 3, epsabs=epsabs)
    return F


'''
#Fn = np.zeros(Nrkv)
anaFn = np.zeros([Nrkv, Nmu])
for j in range(Nmu):
    for i in range(Nrkv):
#        Fn[i] = F(rkv[i], mu[j])
        anaFn[i, j] = anaF(rkv[i], mu[j])
        print('mu_', j, 'rkv_', i)
#    plt.plot(rkv, Fn)
    plt.plot(rkv, anaFn[:, j], label=r'$\mu/\varepsilon$=%.1f'%mu[j])

np.savetxt('integral.txt', anaFn)
np.savetxt('mu.txt', mu)
    
plt.xlabel(r'$2R/(k_{\varepsilon}^2v)$')
plt.ylabel(r'Integral')
plt.title(r'The results of the integral for $\mu$ is from $-2.1$ to $-1.2$ (analytical)') 

plt.legend()
plt.show()
#print(FF(1, 2, -1))
'''


'''
NOO = 100
OO = np.linspace(-1, 3, NOO)
ff = np.linspace(-1, 3, NOO)
anaff = np.linspace(-1, 3, NOO)
for i in range(NOO):
    ff[i] = f(OO[i], 2, 2, -1)
    anaff[i] = anaf(OO[i], 2, 2, -1)
plt.plot(OO, ff, 'r')
plt.plot(OO, anaff, 'b')
plt.show()
'''
