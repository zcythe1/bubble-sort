import random, time, os
from colorama import Fore

nums = []

for i in range(10): nums.append(random.randint(0, 100))
nums1 = nums
os.system('clear')

print(Fore.WHITE + 'Bubble sort:\n' + Fore.RED)
print(nums)

time_var, moves, decisions, cycles = time.time(), 0, 0, 0

while True:
  moved = False
  
  for i in range(9):
    one = nums[i]
    two = nums[i+1]
    
    decisions += 1
    if one > two:
      nums[i] = two
      nums[i+1] = one
      moves += 1
      moved = True
      
  print(nums)
  cycles += 1
  decisions += 1
  
  if moved == False:
    time_var = time.time() - time_var
    
    print(Fore.GREEN + '\nSorted!')
    print('Solution:')
    print(nums)
    
    print(f'\nTook {time_var} Seconds')
    print(f'Took {decisions} Decisions')
    print(f'Took {moves} Moves')
    print(f'Took {cycles} Cycles')
    break

time_var, descisions, moves, cycles = time.time(), 0, 0, 0

while True:
  nums2 = []
  for i in range(int(len(nums1)/2)):  
    descisions += 1
    if nums1[i*2] > nums1[i*2 + 1]:
      nums2.append(nums1[i*2 + 1])
      nums2.append(nums1[i*2])
      moves += 1
    else:
      nums2.append(nums1[i*2])
      nums2.append(nums1[i*2 + 1])
      print(nums2)
    cycles += 1
  time_var = time.time() - time_var

  
  print(nums2)
  break

  
  """
  if len(nums1) % 2 != 0:
    nums2[-1].append(nums1[-1])
  """