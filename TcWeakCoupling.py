from nsr import *

f0 = np.zeros(Nrkv)
f1 = np.zeros(Nrkv)
densityTc = np.zeros(Nrkv)

for i in range(Nrkv):
    print('rkv_', i, '=', rkv[i])
    f0[i] = F(rkv[i], -1e-3)
    print('f0_', i, '=', f0[i])
    f1[i] = F(rkv[i], -.1)
    print('f1_', i, '=', f1[i])
    densityTc[i] = - (f0[i] - f1[i]) / .1
    print('density_', i, '=', densityTc[i])
    
x = np.zeros(Nrkv)
y = np.zeros(Nrkv)
for i in range(Nrkv):
    x[i] = rkv[i]/(densityTc[i]**(2/3))
    y[i] = 1/(densityTc[i]**(2/3))
plt.plot(x, y)

paperDataTc = np.loadtxt('./paperDataTc.csv', delimiter=',')
plt.plot(paperDataTc[:, 0], paperDataTc[:, 1])

plt.xlabel(r'$2R/(k_n^2 v)$')
plt.ylabel(r'$k_BT_C/E_n$')
plt.show()
