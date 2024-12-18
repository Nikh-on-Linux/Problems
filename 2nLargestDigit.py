'''
Find the second largest digit of number
'''

userInput = int(input('Enter the number: '))
def find2ndLargestNum(num):
  nums = []
  for _ in range(0,len(str(num))):
    nums.append(num%10)
    num //= 10
  for j in range(0,len(nums)):
    for k in range(j+1,len(nums)):
      if nums[j] > nums[k]:
        nums[j],nums[k] = nums[k],nums[j]
  
  return nums[len(nums)-2]

print(f"the secondlargest number is {find2ndLargestNum(userInput)}")