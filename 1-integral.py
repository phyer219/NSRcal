from nsr import *

printParamaters()

#Fn = np.zeros(Nrkv)
Fn = np.zeros([Nrkv, Nmu])
for j in range(Nmu):
    for i in range(Nrkv):
#        Fn[i] = F(rkv[i], mu[j])
        Fn[i, j] = F(rkv[i], mu[j])
        print("Now calculating ...mu_%i rkv_%i \r"%(j, i), end='')
#    plt.plot(rkv, Fn)
    plt.plot(rkv, Fn[:, j], label=r'$\mu/\varepsilon$=%.1f'%mu[j])



plt.xlabel(r'$2R/(k_{\varepsilon}^2v)$')
plt.ylabel(r'Integral')
plt.title(r'The results of the integral for $\mu$ is '
          'from $%.1f$ to $%.1f$ (analytical)'%(Amu, Bmu)) 
plt.legend()

# ----------------------SAVE----------------------------------
np.savetxt('./data/%s-integral.txt'%mark, Fn)
np.savetxt('./data/%s-mu.txt'%mark, mu)
plt.savefig('./fig/%s-integral.png'%mark)
# ----------------------SAVE----------------------------------


print("-----------------------------------------------")
print("-----------1-integral COMPLETE!----------------")
print("-----------------------------------------------")
"""
else:
    print("-----------------------------------------------")
    print("-----------1-integral SKIP!    ----------------")
    print("-----------------------------------------------") 
"""
