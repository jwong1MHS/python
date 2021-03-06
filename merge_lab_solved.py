import random

#This is here for later use
def rand_list(n, limit):
    g = []
    while (n > 0):
        g.append(random.randrange(limit))
        n-= 1
    return g


#==================================================
# Problem 0

# Base your answers on the following lists:
a = [1, 3, 4, 8, 9]
b = [2, 5, 6, 7]

# i) What is significant about the order of the elements in these lists?
#==============
# Your answer here
# Both lists are in ascending order.
#==============

# ii) Manually set the list a_and_b such that it contains the same elements
#     as lists a and b in ascending order. Do not use a or b, just type the
#     correct sequence of values.
#==============
# Your answer here
a_and_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#==============

# iii) Describe how you constructed the list a_and_b in part ii
#==============
# Your answer here
# Compared the first values in each list, took the samllest one.
# Kept looking at the next values, moving over after picking one for the new list.
#==============

# End Problem 0
#==================================================


#==================================================
# Problem 1
print("\n==================================================")
print("Problem 1")
# Write the following function, thinking about the process you
# used in Problem 0

# Precondition: a and b are lists sorted in ascending order
# Returns a new list combining all the elements of a and b.
# The returned list must be in ascending order
def merge_lists(a, b):
    new_list = []
    #==============
    apos = 0
    bpos = 0
    while apos < len(a) and bpos < len(b):
        if a[apos] < b[bpos]:
            new_list.append(a[apos])
            apos+= 1
        else:
            new_list.append(b[bpos])
            bpos+= 1
    if apos < len(a):
        new_list+= a[apos:]
    if bpos < len(b):
        new_list+= b[bpos:]
    #==============
    return new_list

#Test merge_lists
a = [1, 3, 4, 8, 9]
b = [2, 5, 6, 7]
c = [0, 5, 10]
print(merge_lists(a, b))
print(merge_lists(a, c))

# End Problem 1
#==================================================


#==================================================
# Problem 2
print("\n==================================================")
print("Problem 2")
# Random lists needed to try new things out
g0 = rand_list(10, 10)
g1 = rand_list(10, 10)
# There is a python function sorted()
# It will take a list as a parameter, and return a new list with its
# elements in ascending order.

# Modify g0  and g1 such that the following print statement produces a sorted list
# Do not write a function.
# Uncomment the print statements to test your answer.

print( g0 )
print ( g1 )
#==============
# Your code here
g0 = sorted(g0)
g1 = sorted(g1)

#==============
print( g0 )
print ( g1 )
print( merge_lists(g0, g1) )


# End Problem 2
#==================================================


#==================================================
# Problem 3
print("\n==================================================")
print("Problem 3")
# Yet another, bigger, random list
g2 = rand_list(20, 100)

# i) Split g2 into 2 evenly sized halves, assign new variables to each half.
# Do not write a function.
#==============
# Your code here
g2_0 = g2[:50]
g2_1 = g2[50:]
#==============

# ii) Perform the same operations on your 2 halves of g2 that
#     you did on g0 and g1 to create and print a single sorted list.
#     You must use merge and sorted, but sorted cannot be your outermost function.
# Do not write a function
# Uncomment the print statement below to test
#==============
# Your code here
g2_0 = sorted(g2_0)
g2_1 = sorted(g2_1)
#==============
print( merge_lists(g2_0, g2_1) )

# End Problem 3
#==================================================


#==================================================
# Problem 4
print("\n==================================================")
print("Problem 4")
# Do you have any idea what sorted does? -No
# What kind of magics does it require? -Unknown
# Let us use our own magics then!
#
# merge_sort will take any list and return a new list, containting
# all the same elements, in ascending order.
# Use the knowledge you have ganied from the previous problems.
# You MUST use mrege_lists
# You CANNOT use sorted! or any other python provided function that sorts things

def merge_sort(g):
    # Sometimes, this function doesn't need to do any work
    # If all you can tell is the size of a list, how can you tell
    # it is in order?
    if ( len(g) <= 1 ):
        return g

    # In any other case, we must do something, Let's make 2 smaller lists to work on
    #==============
    # Your code here
    mid = len(g) // 2;
    g0 = g[:mid]
    g1 = g[mid:]
    #==============

    # If you have 2 lists, you can call merge_lists.
    # But wait! You say, they must be sorted to use merge_lists, and I cannot use sorted()
    # If only you had another function that takes a list and returns it in order...
    # Perhaps you have some of your own dark wizardry to rely on...
    #
    return merge_lists(merge_sort(g0), merge_sort(g1))

# Test merge_sort
g3 = rand_list(20, 100)
print(merge_sort(g3))

# End Problem 4
#==================================================


#==================================================
# Challenge!

# That was too easy you say?
# Merge sort requires you to make lots of copies of the list (or its halves)
# Write new versions of merge_sort and merge such that it does not create any
# new lists or copies of original lists (including slices).
# You will need to change the parameters for merge_sort and merge_lists for this.
