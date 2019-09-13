import numpy as np


#noa = 'num'
noa = 'ana3'
name = 'formal'
mark = '%s-%s'%(noa, name)

rootNum = 10                    # Gaussian Quadrature 积分时取的根的个
                                # 数.
beta = 1                        # 温度的倒数.
zero = 1e-6                     # 积分从零开始时, 为避免发散, 从一个非
                                # 常小的数值开始积.
R = 1/30                        # 参数 k_epsilon R 的取值.
epsabs = 1e-1                   # 用 integrate.quad 积分时限定的绝对误
                                # 差 .

Arkv = -2
Brkv = 2
Nrkv = 100

rkv = np.linspace(Arkv, Brkv, Nrkv)


Amu = -2.1
Bmu = -.2
Nmu = 10
mu = np.linspace(Amu, Bmu, Nmu)

def printParamaters():
    print('')
    print('-----------------------------------------------')
    print('------------PARAMATERS-------------------------')
    print('-----------------------------------------------')
    print("noa = %s"%noa)
    print('Marker is mark = %s'%mark)
    print('Root number of Gaussian Quadrature is rootNUm =', rootNum)
    print('Temperature is beta =', beta)
    print('Paramater k_epsilon R =', R)
    print('Small number zero =', zero)
    print('Absolute error epsabs =', epsabs)
    print('mu is in [Amu, Bmu] = [%.1f, %.1f] cut into Nmu = %i'
          %(Amu, Bmu, Nmu))
    print("rkv is in [Arkv, Brkv] = [%.1f, %.1f] cut into Nrkv = %i"
          %(Arkv, Brkv, Nrkv))
    print('-----------------------------------------------')
    print('-----------------------------------------------')
    return None

para = open('./data/%s-Paramaters.txt'%mark, mode='w')
para.write('-----------------------------------------------\n')
para.write('------------PARAMATERS-------------------------\n')
para.write('-----------------------------------------------\n')
para.write('Marker is mark = %s\n'%mark)
para.write('Root number of Gaussian Quadrature is rootNUm =%i\n'
           %rootNum)
para.write('Temperature is beta = %i\n'%beta)
para.write('Paramater k_epsilon R = %.3f\n'%R)
para.write('Small number zero = %f\n'%zero)
para.write('Absolute error epsabs = %f\n'%epsabs)
para.write('mu is in [Amu, Bmu] = [%.1f, %.1f] cut into Nmu = %i\n'
           %(Amu, Bmu, Nmu))
para.write('rkv is in [Arkv, Brkv] = [%.1f, %.1f] cut intoNrkv'
           '=%i\n'%(Arkv, Brkv, Nrkv))
para.write('-----------------------------------------------\n')
para.write('-----------------------------------------------\n')
para.close()
