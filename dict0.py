def get_frequencies(g):
    frequencies = {}
    for thing in g:
        if thing in frequencies:
            frequencies[thing]+= 1
        else:
            frequencies[thing] = 1
    return frequencies

print(get_frequencies( [6, -23, 8, 9, -23, 8, 5.4, 6, 9, -23] ))

def lists2dict(g0, g1):
    d = {}
    i = 0
    while i < len(g0):
        d[ g0[i] ] = g1[i]
        i+= 1
    return d

print(lists2dict(['v', 'viii', 'iv'], ['empire strikes back', 'force awakens', 'new hope']))

def combine_dict(d0, d1):
    newd = {}
    for key in d0:
        newd[key] = [ d0[key] ]
    for key in d1:
        if key in newd:
            newd[key].append( d1[key] )
        else:
            newd[key] = [ d1[key] ]
    return newd

print( combine_dict( {'a' : 'apple', 'z' : 'zed', 'q' : 'quixotic'}, {'b' : 'boba', 'a' : 'akbar', 'z' : 'zoo', 'w' : 'wombat' }) )