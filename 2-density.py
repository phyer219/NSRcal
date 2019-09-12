from nsr import *

anaFn = np.loadtxt('./data/%s-integral.txt'%mark)
mu = np.loadtxt('./data/%s-mu.txt'%mark)
rkv = np.loadtxt('./data/%s-rkv.txt'%mark)

Nrkv, Nmu = anaFn.shape

print(anaFn.shape)
print(mu)

dd = mu[1] - mu[0]

density = np.zeros([Nrkv, Nmu-2])
for j in range(Nmu-2):
    for i in range(Nrkv):
        density[i, j] = anaFn[i, j+2] -anaFn[i, j]
        density[i, j] = - density[i, j] / (2*dd)
print(density)

for i in range(Nmu-2):
    plt.plot(rkv, density[:, i],
             label=r'$\mu/\varepsilon$=%.1f'%mu[i+1])

plt.xlabel(r'$2R/(k_{\varepsilon}^2v)$')
plt.ylabel(r'$n/n_{\varepsilon}$')
plt.title(r'The results of density for $\mu$ is from $-2$ to$-1.3$')

plt.legend()

np.savetxt('./data/%s-density.txt'%mark, density)
plt.savefig('./fig/%s-density.png'%mark)

#plt.show()
