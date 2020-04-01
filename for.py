def count(key, data):
    c = 0
    for e in data:
        if e == key:
            c+= 1
    return c

print(count(4, [1, 2, 3, 4]))
print(count('a', 'abracadabra'))

def doublify(g):
    new_g = []
    for e in g:
        new_g.append(e * 2)
    return new_g

print(doublify([6, 3, -8, 3.5]))

def add_ten(g):
    i = 0
    while i < len(g):
        g[i]+= 10
        i+= 1
g = [1, 2, 3, 4]                                                                                                                                                                                                          
add_ten(g)                                                                                                                                                                                                                
print(g)  