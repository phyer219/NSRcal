from nsr import *
# ----------------------LOAD ---------------------------------
density = np.loadtxt('./data/%s-density.txt'%mark)
F = np.loadtxt('./data/%s-integral.txt'%mark)
paperData = np.loadtxt('paperDataEnergy.csv', delimiter=",")
# ----------------------LOAD ---------------------------------
cordinate = np.zeros(Nmu-2)

for i in range(Nmu-2):
    d = np.abs(density[0, i] - 1)
    for j in range(Nrkv):
        if np.abs(density[j, i]-1) < d:
            d = np.abs(density[j, i]-1)
            cordinate[i] = j



energy = np.zeros(Nmu-2)
x = np.zeros(Nmu-2)
for i in range(Nmu-2):
    c = int(cordinate[i])
    energy[i] = F[c, i] + mu[i]
    x[i] = rkv[c]

plt.scatter(x, energy)
plt.plot(paperData[:, 0], paperData[:, 1])



# ----------------------SAVE ---------------------------------
np.savetxt('./data/%s-result-x.txt'%mark, x)
np.savetxt('./data/%s-result-y.txt'%mark, energy)

plt.savefig('./fig/%s-result.png'%mark)
# ----------------------SAVE ---------------------------------
print("-----------------------------------------------")
print("-------------3-energy COMPLETE!----------------")
print("-----------------------------------------------")


#plt.show()
