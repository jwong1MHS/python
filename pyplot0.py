import matplotlib.pyplot as plt
import random

NUM_VALS = 10
NUM_DOTS = 100

linear_y = []
quadratic_y = []
exponent_y = []

i=0
while i < NUM_VALS:
    linear_y.append(i)
    quadratic_y.append(i**2)
    exponent_y.append(2**i)
    #yvals.append( random.randrange(0, 100) )
    i+= 1
    
plt.plot(linear_y)
plt.plot(quadratic_y)
plt.plot(exponent_y)
plt.show()


xvals = []
yvals = []
scale = []
i = 0
while i < NUM_DOTS:
    xvals.append( random.randrange(1, 50) )
    yvals.append( random.randrange(1, 50) )
    scale.append( xvals[i] / yvals[i] * 10)
    #yvals.append( int(random.normalvariate(50, 10)) )
    i+= 1

plt.scatter(xvals, yvals, scale)
plt.show()