import matplotlib.pyplot as plt
from random import randrange, normalvariate

pops_2010 = [1585873,2504700,2230722,1385108,468730]
labels = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']

plt.bar(labels, pops_2010)
plt.show()

NUM_VALS = 100000
randos = []
i = 0
while i < NUM_VALS:
    randos.append( randrange(0, 100) )
    i+= 1
plt.hist( randos, 10)
plt.show()
plt.hist( randos, 50 )
plt.show()

normal_randos = []
i = 0
while i < NUM_VALS:
    normal_randos.append( normalvariate(50, 1) )
    i+= 1
    
plt.hist( normal_randos, 25)
plt.show()
plt.hist( normal_randos, 100)
plt.show()


