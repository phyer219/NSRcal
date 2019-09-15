from paramaters import *
import numpy as np
from matplotlib import pyplot as plt
# ----------------------LOAD ---------------------------------
for i in ('ana1', 'ana2', 'ana3'):
    x = np.loadtxt('./data/%s-%s-result-x.txt'%(i, name))
    y = np.loadtxt('./data/%s-%s-result-y.txt'%(i, name))
    plt.scatter(x, y, marker='x', label=i)
# ----------------------LOAD ---------------------------------
paperData = np.loadtxt('paperDataEnergy.csv', delimiter=",")
plt.plot(paperData[:, 0], paperData[:, 1])

plt.legend()
plt.savefig('./fig/co-result.png')

print("-----------------------------------------------")
print("-------------- CO-FIG COMPLETE!----------------")
print("-----------------------------------------------")


#plt.show()
