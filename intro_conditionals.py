def diff21(n):
  if n > 21:
    return (n - 21) * 2
  else:
    return 21 - n
print("diff21 tests:")
print(diff21(19))
print(diff21(10))
print(diff21(21))


def fix_teen(n):
  if n < 20 and n > 12:
    if n == 15 or n == 16:
      return n
    else:
      return 0
  else:
    return n

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
print("no_teen_sum tests:")
print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


def sorta_sum(a, b):
  s = a + b
  if s > 9 and s < 20:
    return 20
  else:
    return s
print("sorta_sum tests:")
print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))

def lone_sum(a, b, c):
  s = a + b + c
  if a == b:
    if a == c:
      return 0
    else:
      return c
  else:
    if a == c:
      return b
    if b == c:
      return a
    else:
      return s
print("lone_sum tests:")
print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))

def lucky_sum(a, b, c):
  if a == 13:
      return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c
print("lucky_sum tests:")
print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))

def round10(n):
  if n % 10 < 5:
    return n - (n % 10)
  else:
    return (n // 10 + 1) * 10

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
print("round_sum tests:")
print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))

def make_bricks(small, big, goal):
  #first find out how many big bricks we would need if we had infinite big bricks
  big_total = goal // 5

  #if the optimal # of big bricks needed is less than the amount provided,
  #then that will be the number of big bricks used.
  #otherise, we will just have to use all the big bricks available
  if big_total <= big:
    big = big_total

  #once we know how many big bricks we can use, subtract that total
  #from the goal
  goal = goal - (5 * big)

  #what's left is the number of small bricks needed to finish, if
  #that is <= the number of small bricks available, we good!
  return goal <= small

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
