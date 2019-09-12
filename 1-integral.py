from nsr import *

Arkv = 0
Brkv = 3
Nrkv = 10

rkv = np.linspace(Arkv, Brkv, Nrkv)


Amu = -2.1
Bmu = -1.2
Nmu = 5
mu = np.linspace(Amu, Bmu, Nmu)


#Fn = np.zeros(Nrkv)
anaFn = np.zeros([Nrkv, Nmu])
for j in range(Nmu):
    for i in range(Nrkv):
#        Fn[i] = F(rkv[i], mu[j])
        anaFn[i, j] = anaF(rkv[i], mu[j])
        print('mu_', j, 'rkv_', i)
#    plt.plot(rkv, Fn)
    plt.plot(rkv, anaFn[:, j], label=r'$\mu/\varepsilon$=%.1f'%mu[j])


    
plt.xlabel(r'$2R/(k_{\varepsilon}^2v)$')
plt.ylabel(r'Integral')
plt.title(r'The results of the integral for $\mu$ is from $%.1f$ to $%.1f$ (analytical)'%(Amu, Bmu)) 
plt.legend()

np.savetxt('./data/%s-integral.txt'%mark, anaFn)
np.savetxt('./data/%s-mu.txt'%mark, mu)
np.savetxt('./data/%s-rkv.txt'%mark, rkv)
plt.savefig('./fig/%s-integral.png'%mark)

#plt.show()
#print(FF(1, 2, -1))
