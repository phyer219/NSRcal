from nsr import *

if noa=='num' or noa=='ana1' or noa=='ana2':
    """数值微分求 density."""
    # ----------------------LOAD ---------------------------------
    Fn = np.loadtxt('./data/%s-integral.txt'%mark)
    mu = np.loadtxt('./data/%s-mu.txt'%mark)
    # ----------------------LOAD----------------------------------

    dd = mu[1] - mu[0]
    Nmu = Nmu - 2
    density = np.zeros([Nrkv, Nmu])
    for j in range(Nmu):
        for i in range(Nrkv):
            density[i, j] = Fn[i, j+2] -Fn[i, j]
            density[i, j] = - density[i, j] / (2*dd)
    for i in range(Nmu):
        plt.plot(rkv, density[:, i],
                 label=r'$\mu/\varepsilon$=%.1f'%mu[i+1])

elif noa=='ana3':
    """解析求 density."""
    def anaDensity(q, rkv, mu):
        a = q**2/2 - 2*mu - rkv
        anaDensity = 3*q**2 / (np.exp(beta*a) - 1)
        return anaDensity

    density = np.zeros([Nrkv, Nmu])
    for j in range(Nmu):
        for i in range(Nrkv):
            density[i, j], err = integrate.quad(lambda x:anaDensity(x, rkv[i], mu[j]), 0, 3, epsabs=epsabs) 
    for i in range(Nmu):
        plt.plot(rkv, density[:, i],
                 label=r'$\mu/\varepsilon$=%.1f'%mu[i])


print("density is")
print(density)


plt.xlabel(r'$2R/(k_{\varepsilon}^2v)$')
plt.ylabel(r'$n/n_{\varepsilon}$')
plt.title(r'The results of density for $\mu$ is from $%.1f$ '
          'to$%.1f$'%(Amu, Bmu))

plt.legend()

# ----------------------SAVE----------------------------------
np.savetxt('./data/%s-density.txt'%mark, density)
plt.savefig('./fig/%s-density.png'%mark)
# ----------------------SAVE----------------------------------

print("-----------------------------------------------")
print("-----------2-density COMPLETE!-----------------")
print("-----------------------------------------------")
