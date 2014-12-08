from math import pow

__author__ = "Aaron Koeppel"
__version__ = 1.0

class Factors(object):
   def __init__(self, i, n):
      self.i = float(i) / 100
      self.n = n
      self.mult = 1
   
   def print_data(self):
      print "i = %.03f" % self.i
      print "n = %d" % self.n

def FoP(factor):
   return pow(1 + factor.i, factor.n)

def PoF(factor):
   return pow(1 + factor.i, factor.n)


def PoA(factor):
   top = pow(1 + factor.i, factor.n) - 1
   bottom = factor.i * pow(1 + factor.i, factor.n)
   return top / bottom

def AoP(factor):
   return 1 / PoA(factor)

def FoA(factor):
   return (pow(1 + factor.i, factor.n) - 1) / factor.i

def AoF(factor):
   return 1 / FoA(factor)

def AoG(factor):
   first = 1 / factor.i
   second = factor.n / (pow(1 + factor.i, factor.n) - 1)
   return first - second

def PoG(factor):
   top = pow(1 + factor.i, factor.n) - factor.i * factor.n - 1
   bottom = pow(factor.i, 2) * pow(1 + factor.i, factor.n)
   return top / bottom