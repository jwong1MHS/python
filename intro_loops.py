def sumFromZeroToN(n):
  s = 0
  while (n > 0):
    s = s + n
    n = n - 1
  return s
print("sumFromZeroToN tests:")
print(sumFromZeroToN(-3))
print(sumFromZeroToN(4))
print(sumFromZeroToN(10))

def sumAtoB(a,b):
  s = 0
  while a <= b:
    s = s + a
    a = a + 1
  return s
print("subAtoB tests:")
print(sumAtoB(0, 1))
print(sumAtoB(1, 3))
print(sumAtoB(2, 0))

def fiveSumFromZeroToN(n):
  s = 0
  while n > 0:
    if n % 5 == 0:
      s = s + n
    n = n - 1
  return s
print("fiveSumFromZeroToN tests:")
print(fiveSumFromZeroToN(0))
print(fiveSumFromZeroToN(10))
print(fiveSumFromZeroToN(33))

def specialSumInclusive(n):
  s = 0
  while n > 0:
    if n % 5 == 0 or n % 3 == 0:
      s = s + n
    n = n - 1
  return s
print("specialSumInclusive tests:")
print(specialSumInclusive(0))
print(specialSumInclusive(3))
print(specialSumInclusive(5))

def specialSumExclusive(n):
  s = 0
  while n > 0:
    if n % 35 == 0:
      s = s + n
    n = n - 1
  return s
print("specialSumExclusive tests:")
print(specialSumExclusive(5))
print(specialSumExclusive(7))
print(specialSumExclusive(35))

def sumOfFirstNSquares(n):
  s = 0
  while n > 0:
    s = s + n**2
    n = n - 1
  return s
print("sumOfFirstNSquares tests:")
print(sumOfFirstNSquares(1))
print(sumOfFirstNSquares(2))
print(sumOfFirstNSquares(3))

def sumSquaresBetween(a,b):
  s = 0
  n = int(b**.5)
  while n**2 >= a:
    s = s + n**2
    n = n - 1
  return s
print("sumSquaresBetween tests:")
print(sumSquaresBetween(30, 101))
print(sumSquaresBetween(1, 10))
print(sumSquaresBetween(5, 10))

def sumOfPowers(n):
  s = 0
  i = 1
  while 2**i <= n:
    s = s + 2**i
    i = i + 1
  return s
print("sumOfPowers tests:")
print(sumOfPowers(0))
print(sumOfPowers(10))
print(sumOfPowers(2))

def sumDigits(n):
  s = 0
  n = abs(n)
  while n > 0:
    s = s + n % 10
    n = n // 10
  return s
print("sumDigits tests:")
print(sumDigits(123))
print(sumDigits(19))
print(sumDigits(-25))

def countDigits(n):
  count = 1
  n = abs(n)
  while n > 9:
    count = count + 1
    n = n // 10
  return count
print("countDigits tests:")
print(countDigits(0))
print(countDigits(4))
print(countDigits(12))

def countOddDigits(n):
  count = 0
  n = abs(n)
  while n > 0:
    if n % 10 % 2 == 1:
      count = count + 1
    n = n // 10
  return count
print("countOddDigits tests:")
print(countOddDigits(111))
print(countOddDigits(134))
print(countOddDigits(2))


def isPrime(n):
  return n == 2 or n == 3 or n == 5 or n == 7

def countPrimeDigits(n):
  count = 0
  n = abs(n)
  while n > 0:
    if isPrime(n % 10):
      count = count + 1
    n = n // 10
  return count
print("countPrimeDigits tests:")
print(countPrimeDigits(123))
print(countPrimeDigits(12345))
print(countPrimeDigits(123456))
