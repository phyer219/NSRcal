from nsr import *

#density = np.loadtxt('./data/%s-density.txt'%mark)

paperDataTc = np.loadtxt('./paperDataTc.csv', delimiter=',')





def anaDensity(q, rkv, mu):
    a = q**2/2 - 2*mu - rkv
    anaDensity = 3*q**2 / (np.exp(beta*a) - 1)
    return anaDensity


a = np.zeros(Nrkv)
for i in range(Nrkv):
    a[i], err = integrate.quad(lambda x:anaDensity(x, rkv[i], 0),0,
                            10, epsabs=epsabs)

x = rkv/a**(2/3)
y = 1/a**(2/3)


plt.plot(x, y)

plt.plot(paperDataTc[:, 0], paperDataTc[:, 1])

plt.show()





'''
plt.xlabel(r'$2R/(k_n^2 v)$')
plt.ylabel(r'$k_BT_C/E_n$')
plt.show()
'''
