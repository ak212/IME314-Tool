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
   try:
      return top / bottom
   except ZeroDivisionError:
      return "NaN"

def AoP(factor):
   if str(PoA(factor)).isalpha():
      return PoA(factor)
   else:
      return 1 / PoA(factor)

def FoA(factor):
   try:
      return (pow(1 + factor.i, factor.n) - 1) / factor.i
   except ZeroDivisionError:
      return "NaN"

def AoF(factor):
   if str(FoA(factor)).isalpha():
      return FoA(factor)
   else:
      return 1 / FoA(factor)


def AoG(factor):
   try:
      first = 1 / factor.i
      second = factor.n / (pow(1 + factor.i, factor.n) - 1)
      return first - second
   except ZeroDivisionError:
      return "NaN"


def PoG(factor):
   try:
      top = pow(1 + factor.i, factor.n) - factor.i * factor.n - 1
      bottom = pow(factor.i, 2) * pow(1 + factor.i, factor.n)
      return top / bottom
   except ZeroDivisionError:
      return "NaN"


def switch(x, factor):
   return{
          1: FoP(factor),
          2: PoF(factor),
          3: PoA(factor),
          4: AoP(factor),
          5: FoA(factor),
          6: AoF(factor),
          7: AoG(factor),
          8: PoG(factor)
          }[x]

def cycle(flag=0):
   print "Choose Function:"
   
   if flag == 1:
      print "1. F/P"
      print "2. P/F"
      print "3. P/A"
      print "4. A/P"
      print "5. F/A"
      print "6. A/F"
      print "7. A/G"
      print "8. P/G"
      print "9. Quit"
      
   choice = " "
   
   while choice not in range(0, 10):
      choice = int(raw_input())
      
   if choice != 9:
      i = raw_input("i% = ")
      n = int(raw_input("n = "))
      
      factor = Factors(i, n)
      factor.print_data()
      answer = switch(choice, factor)
      
      if type(answer) == 'float':
         print "answer = %.04f" % answer
      else:
         print answer
   
   return choice

def main():
   choice = cycle(1)
   
   while choice != 9:
      choice = cycle()

if __name__ == '__main__':
   main()
