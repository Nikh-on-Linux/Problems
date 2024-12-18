'''
Write a Python program that prints all numbers between 1 and 300 in reverse order, which
are divisible by both 2 and 3 but not divisible by 5. 
'''

nums = []
for i in range(0,300):
  if i%2 == 0 or i%3 == 0 and i%5 !=0 :
    nums.append(i)   
    
for j in reversed(nums):
  print(j)