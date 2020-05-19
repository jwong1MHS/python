import random

def rand_list(n, limit):
    g = []
    while (n > 0):
        g.append(random.randrange(limit))
        n-= 1
    return g

def bin_search(g, key, low, high):
    if ( low > high ):
        return -1

    mid = (low + high) // 2
    guess = g[mid]
    if ( guess == key ):
       return mid

    elif ( guess > key ):
        return bin_search(g, key, low, mid - 1)

    elif ( guess < key ):
        return bin_search(g, key, mid + 1, high)


#For testing, make a list of random numbers, but add a specific number so I know it is in the list.
a = rand_list(100000, 1000)
a.append(387)
a = sorted(a)

found = bin_search(a, 387, 0, len(a))
print(found, a[found])

#look for a value I know won't be in the list.
#the list only has integers, so I know a floating point value won't show up
found = bin_search(a, 583.47, 0, len(a))
print(found, a[found])