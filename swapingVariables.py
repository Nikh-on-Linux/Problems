'''
Write a program for swapping a number with using temporary variable and without using
temporary variable. 
'''

#Swaping using temp variable
def tempVar(a,b):
  temp = a
  a = b
  b = temp
  print(f"Swapping variable using temporary variable a={a} b={b}")

#Swaping using XOR operator
def xorOperator(a,b):
  a = a^b
  b = a^b
  a = a^b
  print(f"Swapping variable using XOR operator a={a} b={b}")
  
#Swaping using arithmetic operation
def arthOperation(a,b):
  a = a-b
  b = a+b
  a = b-a
  print(f"Swapping variable using arithmetic operation a={a} b={b}")
  

a = int(input("Enter first variable: "))
b = int(input("Enter second variable: "))
print(f"Original input a={a} b={b}")
tempVar(a,b)
xorOperator(a,b)
arthOperation(a,b)