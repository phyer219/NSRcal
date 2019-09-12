from nsr import *

density = np.loadtxt('./data/%s-density.txt'%mark)
mu = np.loadtxt('./data/%s-mu.txt'%mark)
anaF = np.loadtxt('./data/%s-integral.txt'%mark)
rkv = np.loadtxt('./data/%s-rkv.txt'%mark)

Nrkv, Nmu = density.shape
Nmu = Nmu + 2

cordinate = np.zeros(Nmu-2)

for i in range(Nmu-2):
    d = np.abs(density[0, i] - 1)
    for j in range(Nrkv):
        if np.abs(density[j, i]-1) < d:
            d = np.abs(density[j, i]-1)
            cordinate[i] = j

print(cordinate)

energy = np.zeros(Nmu-2)
x = np.zeros(Nmu-2)
for i in range(Nmu-2):
    c = int(cordinate[i])
    energy[i] = anaF[c, i] + mu[i]
    print(density[c, i])
    x[i] = rkv[c]

plt.scatter(x, energy)

plt.savefig('./fig/%s-result.png'%mark)

#plt.show()
