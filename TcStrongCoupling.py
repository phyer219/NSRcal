from nsr import *


def delta(omega, q, rkv, mu):
    """函数 delta^p .
    纯数值会用到.
    ana1 会用到."""
    if noa=='num':
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
    return rel


Nmu = 1000
Nrkv = 20
mu = np.linspace(-80, -1e-2, Nmu)
rkv = np.linspace(2, 100, Nrkv)

muRoot = np.zeros(Nrkv)
y = np.zeros(Nmu)
# 一条线对应于一个给定的 rkv . 横坐标对应于 mu . 找到纵坐标为 0 时对应
# 的 mu . 然后算出这时给定 rkv 和 mu 时的 density ,就可以得到 Tc.
for j in range(Nrkv):
    c = 0
    for i in range(Nmu):
        y[i] = delta(0, 0, rkv[j], mu[i])
        if np.abs(y[i])<np.abs(y[c]):
            c = i
    print('y_', c, '=', y[c])
    muRoot[j] = mu[c]

    plt.plot(mu, y, label=r'$2R/(k_{\epsilon}^2v)=%.1f$'%rkv[j])
plt.legend()
plt.xlabel(r'$\mu/\epsilon$')
plt.ylabel(r'$T^{-1}$')
print(muRoot)
plt.show()

'''
"""解析求 density."""
def anaDensity(q, rkv, mu):
    a = q**2/2 - 2*mu - rkv
    anaDensity = 3*q**2 / (np.exp(beta*a) - 1)
    return anaDensity

density = np.zeros([Nrkv])

for i in range(Nrkv):
    sp = 4*muRoot[i] + 2*rkv[i]
    sp = np.sqrt(np.abs(sp))
    a, err = integrate.quad(lambda x:anaDensity(x, rkv[i], muRoot[i]),0,
                            sp-zero, epsabs=epsabs)
    b, err = integrate.quad(lambda x:anaDensity(x, rkv[i], muRoot[i]),
                            sp+zero, 10, epsabs=epsabs)
    density[i] = a + b


x = rkv/a**(2/3) /beta
y = 1/density**(2/3)

print("density is")
print(density)

plt.plot(x, y)

plt.show()
'''
