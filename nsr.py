from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate

from scipy.integrate import fixed_quad
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from scipy.special import roots_legendre as leg

from paramaters import *

# noa = 'num'
# 定义用到的函数.
def xi(k, mu):
    return k**2 - mu
def n(k, mu):
    x = xi(k,mu)
    n =  1 / (np.exp(beta*x) - 1)
    return n
def z(omega, q, mu):
    return omega - q**2/2 + 2*mu
def pi(omega, q, k, mu):
    """没有积分时的 PI. 
    只有纯数值 num 会用到."""
    pi = 1 + n(k+q/2, mu) + n(-k+q/2, mu)
    pi = pi / (2*k**2 - z(omega, q, mu))
    pi = pi * k**4
    pi = pi -k**2/2 - z(omega, q, mu)/4
    pi = 2*pi / np.pi**2 * R
    return pi
def PI(omega, q, mu):
    """将函数 pi 中的 k 积分掉.
    只有纯数值 num 会用到."""
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
        PI1, err = fixed_quad(lambda x: pi(omega, q, x, mu), zero,
                              a-zero, n=rootNum) 
        PI2, err = fixed_quad(lambda x: pi(omega, q, x, mu), a+zero,
                              10, n=rootNum)
        PI = PI1 + PI2
    return PI
def delta(omega, q, rkv, mu):
    """函数 delta^p .
    只有纯数值会用到."""
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
    """函数 delta^p .
    只 ana1 会用到."""
    a = q**2/2 - 2*mu - rkv
    if omega<a:
        anaDelta = 0
    else:
        anaDelta = -np.pi
    return anaDelta

def f(omega, q, rkv, mu):
    """未积分的积分.
    num 会用到.
    ana1 会用到."""
    if noa=='num':
        f = 1 / (np.exp(beta*omega) - 1)
        f = 3*f / np.pi
        f = f * delta(omega, q, rkv, mu)
    elif noa=='ana1':
        f = 1 / (np.exp(beta*omega) - 1)
        f = 3*f / np.pi
        f = f * anaDelta(omega, q, rkv, mu)
    else:
        print('-----------NOA ERROR!----------')
        f = 0
    return f
def FF(q, rkv, mu):
    """把 omega 积掉的积分.
    num 会用到.
    ana1 会用到."""

    FF, err = integrate.quad(lambda x:f(x, q, rkv, mu), -1.1, 10,
                             epsabs=epsabs)
    return FF
def anaf(q, rkv, mu):
    """没有积掉 q 的解析表达式.
    ana2 会用到.
    ana3 会用到."""
    a = q**2/2 - 2*mu - rkv
    anaf = 3*np.log(np.abs(1 - np.exp(-beta * a))) / beta
    anaf = q**2 * anaf
    return anaf
def F(rkv, mu):
    """把 omega 和 q 积掉的积分.
    num 会用到.
    ana1 会用到.
    ana2 会用到
    ana3 会用到"""
    if noa=='num' or noa=='ana1':
        F, err = integrate.quad(lambda x:x**2*FF(x,rkv, mu), zero, 3,
                                epsabs=epsabs)
    if noa=='ana3' or noa=='ana2':
        F, err = integrate.quad(lambda x:anaf(x,rkv, mu), zero, 3,
                                epsabs=epsabs)
    return F




print(F(1, -2))
