def add(x, y):
   return x+y

def sub(x, y):
   return x-y

def multiply(x, y):
   return x*y

def divide(x, y):
   try:
      return x/y
   except ZeroDivisionError:
      return "Divisor can't be zero"

while True:
   print " 0) add"
   print " 1) sub"
   print " 2) multiply"
   print " 3) divide"
   print "-1) quit"
   print "choice:",
   try:
      nums = []
      userInput = raw_input()
      if userInput == "-1":
         break
      print "Give 2 numbers"
      nums.append(float(raw_input()))
      nums.append(float(raw_input()))
      if userInput == "0":
         print reduce(add, nums)
      if userInput == "1":
         print reduce(sub, nums)
      if userInput == "2":
         print reduce(multiply, nums)
      if userInput == "3":
         print reduce(divide, nums)
   except ValueError:
      print "Not a number, try again"
