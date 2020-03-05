import time

def prob1(n):
    s = 0
    i = 1
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            s+= i
        i+= 1
    return s
print( prob1(10) )
print( prob1(1000) )

def prob6(n):
    square_sum = 0
    sum_squares = 0
    i = 1
    while( i <= n ):
        sum_squares+= i**2
        square_sum+= i
        i+= 1
    square_sum = square_sum**2
    return square_sum - sum_squares
print(prob6(10))
print(prob6(100))



def prob5(n):
    guess = n
    i = 1
    while i <= n:
        if guess % i != 0:
            guess+= 1
            i = 1
        i+= 1
    return guess
now = time.time()
answer = prob5(20)
t = time.time() - now
print("answer: ", answer)
print("time: ", t)
