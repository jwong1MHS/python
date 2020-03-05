def square(x):
  return x * x
print( "square tests:")
print( square(10) )
print( square(5) )
print( square(-2) )

def negate(n):
  return n * -1
print("negate tests:")
print(negate(5))
print(negate(-15))
print(negate(0))

def funkyCalc(x,y,z):
  return (3*x + 0.5 * y)/(2 * z)
print("funkyCalc tests")
print(funkyCalc(1, 1, 1))
print(funkyCalc(3, 2, 1.25))
print(funkyCalc(-1, 6, 1))

def distance(x1,y1,x2,y2):
  s = (x2 - x1)**2 + (y2 - y1)**2
  return s**.5
print("distance tests:")
print(distance(3, 0, 0, 4))
print(distance(1, 0, 2, 0))
print(distance(0, 0, 8, 15))

def ftoc(f):
  return (f-32) * (5/9.0)
print("ftoc tests:")
print(ftoc(32))
print(ftoc(212))
print(ftoc(-40))

def ctof(c):
  return (9.0/5) * c + 32
print(ctof(0.0))
print(ctof(100.0))
print(ctof(-40))

def evalQuadratic(a,b,c,x):
  return a*x**2 + b*x + c
print("evalQuadratic tests:")
print(evalQuadratic(1, 0, 3, 1))
print(evalQuadratic(1, 2, 3, 1))
print(evalQuadratic(1, 0, 3, 2))

def isBig(n):
  return n > 10000
print("isBig tests:")
print(isBig(100))
print(isBig(10000))
print(isBig(10001))

def isEven(n):
  return n%2 == 0
print("isEven tests:")
print(isEven(12))
print(isEven(11))
print(isEven(0))

def sleep_in(weekday, vacation):
  return (not weekday) or vacation
print("sleep_in tests:")
print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile
print("monkey_trouble tests:")
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)
print("parrot_trouble tests:")
print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))

def makes10(a, b):
  return (a == 10) or (b == 10) or ((a + b) == 10)
print("makes10 tests:")
print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))

def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <=10
print("near_hundred tests:")
print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))

def pos_neg(a, b, negative):
  return ((negative and ((a < 0) and (b < 0))) or
          (not negative and ((a < 0 and b >0) or (a > 0 and b < 0))))
print("pos_neg tests:")
print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
