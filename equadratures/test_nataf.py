import numpy as np
from equadratures import *
import matplotlib.pyplot as plt

#---------------------------------------------------------------#
#       list of objects==distributions from parameter
#               testing instance of parameter
#---------------------------------------------------------------#

mean1 = 0.4
var1  = 1.3
low1   = 0.2
up1    = 1.15

mean2 = 0.7
var2  = 3.0
low2   = 0.3
up2    = 0.5

D = list()
D.append(Parameter(order=3, distribution='rayleigh', shape_parameter_A=1.0))
D.append(Parameter(order=3, distribution='rayleigh', shape_parameter_A=4.0))
D.append(Parameter(order=3, distribution='rayleigh', shape_parameter_A=1.0))
D.append(Parameter(order=3, distribution='rayleigh', shape_parameter_A=4.0))
D.append(Parameter(order=3, distribution='uniform', lower=0.05, upper=0.99))
D.append(Parameter(order=3, distribution='uniform', lower=0.5, upper=0.8))
D.append(Parameter(order=3, distribution='gaussian', shape_parameter_A = 1.0, shape_parameter_B=16.0))
D.append(Parameter(order=3, distribution='gaussian', shape_parameter_A = 3.0, shape_parameter_B = 4.0))
#D.append(Parameter(order=3, distribution='Beta', lower=0.0, upper=1.0, shape_parameter_A = 1.4, shape_parameter_B = 2.8))
#D.append(Parameter(order=3, distribution='Beta', lower=0.0, upper=1.0, shape_parameter_A = 3.2, shape_parameter_B = 1.5))
D.append(Parameter(order=3, distribution='gaussian', shape_parameter_A = 3.0, shape_parameter_B = 4.0))
D.append(Parameter(order=3, distribution='gaussian', shape_parameter_A = 3.0, shape_parameter_B = 4.0))
D.append(Parameter(order=3, distribution='gaussian', shape_parameter_A = 1.0, shape_parameter_B=16.0))
D.append(Parameter(order=3, distribution='gaussian', shape_parameter_A = 3.0, shape_parameter_B = 4.0))
#D.append(Parameter(order=3, distribution='Beta', lower=0.0, upper=1.0, shape_parameter_A = 1.0, shape_parameter_B = 1.0))
#D.append(Parameter(order=3, distribution='Beta', lower=0.0, upper=1.0, shape_parameter_A = 1.0, shape_parameter_B = 1.0))
#D.append(Parameter(order=3, distribution='Cauchy', shape_parameter_A = 0.5, shape_parameter_B = 0.7))
#D.append(Parameter(order=3, distribution='Cauchy', shape_parameter_A = 0.8, shape_parameter_B = 0.9))
#D.append(Parameter(order=3, distribution='Chebyshev', upper=1.0, lower=0.0))
#D.append(Parameter(order=3, distribution='Chebyshev', upper=0.99, lower=0.01))
#D.append(Parameter(order=3, distribution='Chisquared', shape_parameter_A=14))
#D.append(Parameter(order=3, distribution='Chisquared', shape_parameter_A=14))
D.append(Parameter(order=3, distribution='exponential', shape_parameter_A = 0.7))
D.append(Parameter(order=3, distribution='exponential', shape_parameter_A = 0.7))
#D.append(Parameter(order=3, distribution='gamma', shape_parameter_A = 1.7, shape_parameter_B = 0.8))
#D.append(Parameter(order=3, distribution='gamma', shape_parameter_A = 0.7, shape_parameter_B = 0.8))
D.append(Parameter(order =3, distribution='rayleigh',shape_parameter_A = 0.7))
D.append(Parameter(order =3, distribution='rayleigh',shape_parameter_A = 0.7))
D.append(Parameter(order=3, distribution='truncated-gaussian',shape_parameter_A = 100., shape_parameter_B =25.0**2, upper = 150., lower = 50.))
D.append(Parameter(order=3, distribution='truncated-gaussian',shape_parameter_A = 100., shape_parameter_B =25.0**2, upper = 150., lower = 50.))
D.append(Parameter(order=3, distribution='weibull', shape_parameter_A=0.8, shape_parameter_B=0.9))
D.append(Parameter(order=3, distribution='weibull', shape_parameter_A=0.8, shape_parameter_B=0.9))


#---------------------------------------------------------------------------#
""" A default correlation matrix is defined in the following for statement:
"""
R = np.identity(len(D))
for i in range(len(D)): 
    for j in range(len(D)):
        if i==j:
            continue
        else:
            R[i,j] = 0.60

""" instance of Nataf class:
    the distribution which belong to the list D will be correlated
    with the matrix R
"""
obj = Nataf(D,R)

""" Random samples are cought inside each distribution
"""
o = obj.getCorrelatedSamples(N=300)
oo = obj.getUncorrelatedSamples(N=300)

""" the following lines select the first two different
    correlated distributions inside the set of
    getCorrelated results.
"""
t = o[:,0]  # correlated 1st
tt = o[:,1] # correlated 2nd

""" Plot of the first two distributions inside
    the set
"""

fig = plt.figure()
plt.grid(linewidth=0.4, color='k')
plt.plot(t, tt,'ro', label='w/o correlations')
plt.plot(oo[:,0], oo[:,1], 'bo', label='w/ correlations')
plt.legend(loc='upper left')
plt.title('getCorrelatedSamples method')
plt.axis('equal')
plt.show()

print '-------------------------------------------------------------------'
print '________test the mean and the variance after getCorrealed:_________'
print 'mean of uncorrelated input: FROM OBJECT', obj.D[0].mean, obj.D[1].mean
#print 'mean of uncorrelated input: AFTER PASSAGE INTO METHOD:', np.mean(t), np.mean(t)
print 'mean of correlated outputs', np.mean(t) , np.mean(tt) 
#print 'variance of uncorrelated inputs', np.var(t[:,0]) , np.var(t[:,1]) 
print 'variance of uncorrelated inputs: FROM OBJECT', obj.D[0].variance, obj.D[1].variance 
#print 'variance of uncorrelated input: AFTER PASSAGE INTO METHOD:', np.var(t[:,0]), np.var(t[:,1])
print 'variance of correlated outputs', np.var(t) , np.var(tt) 
print '-------------------------------------------------------------------'
#------------------------------------------------------#

""" testing transformations: direct
"""
u = obj.C2U(o)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.grid(linewidth=0.4, color='k')
plt.plot(u[:,0], u[:,1],'ro', label='Uncorrelated outputs')
plt.plot(t, tt, 'bo', label='Correlated inputs')
plt.legend(loc='upper left')
plt.title('Nataf transformation')
plt.axis('equal')
adjust_spines(ax, ['left', 'bottom'])
plt.show()


#------------------------------------------------------#
# testing the mean and the variance of output marginals
print '-------------------------------------------------------------------'
print '__testing the mean and the variance after direct nataf transf._____'
print 'direct transformation:'
for i in range(len(D)):
    print 'mean of ',i,'output:', np.mean(u[:,i])
for i in range(len(D)):
    print 'variance of ',i,'output:', np.var(u[:,i])
print '-------------------------------------------------------------------'


#------------------------------------------------------#
""" testing transformations: inverse
"""

c = obj.U2C(u)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.grid(linewidth=0.4, color='k')
plt.plot(c[:,0], c[:,1],'ro', label='correlated out')
plt.plot(u[:,0], u[:,1], 'bo', label='uncorrelated in')
plt.legend(loc='upper left')
plt.axis('equal')
adjust_spines(ax, ['left', 'bottom'])
plt.title('inverse Nataf: check the inverse mapping')
plt.show()

#------------------------------------------------------#
# testing the mean and the variance of output marginals
print '-------------------------------------------------------------------'
print '__testing the mean and the variance after inverse nataf transf.____'
print '-----------------------------------------------'
print 'inverse transformation:'
for i in range(len(D)):
    print 'mean of ',i,'th output:', np.mean(c[:,i])
for i in range(len(D)):
    print 'variance of ',i,'th output:', np.var(c[:,i])
print '-----------------------------------------------'

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.grid(linewidth=0.4, color='k')
plt.plot(c[:,0], c[:,1],'ro', label='correlated out')
plt.plot(t, tt, 'bx', label='correlated in')
plt.legend(loc='upper right')
plt.axis('equal')
adjust_spines(ax, ['left', 'bottom'])
plt.title('inverse Nataf: check the inverse mapping')
plt.show()

