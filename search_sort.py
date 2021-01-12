import random

# Question 1
def counting_sort(lst):

  sorted_lst = []
  maximum = 0
  for i in lst:
    if i > maximum:
      maximum = i
  aux = [0 for i in range(maximum+1)]
  for i in lst:
    aux[i] += 1
  for i in range(len(aux)):
    if aux[i] != 0:
      sorted_lst.append(i)
  return sorted_lst


# Question 2
def ternary_search(lst, target):
  length = len(lst)
  start = 0
  index = -1
  while length >= 1:
    mid1 = start + (length-start) // 3
    mid2 = length - (length-start) // 3

    if target == lst[mid1]:
      return mid1
    elif target == lst[mid2]:
      return mid2
    
    if lst[mid1] > target:
      length = mid1
    elif lst[mid2] > target > lst[mid1]:
      length = mid2
      start = mid1
    elif lst[mid2] < target:
      start = mid2

  return index


# Question 3
def insertion_sort(lst):
  for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
      n = i
      while lst[n] < lst[n-1] and n >= 1:
        lst[n], lst[n-1] = lst[n-1], lst[n]
        n -= 1
  return lst


# Question 4
def nary_search(lst, target, n):
  index = -1

  return index


# Question 5
def jumping_binary_search(sorted_lst, target, jump):
  index = -1
  i = 0
  while True:
    if target <= sorted_lst[jump*i]:
      break
    i += 1
  low = jump*(i-1)
  high = jump*i
  while low <= high:
    mid = (low + high) // 2
    if sorted_lst[mid] < target:
      low = mid + 1
    elif sorted_lst[mid] > target:
      high = mid - 1
    else:
      return mid 
  return index

# This function generates lists of random integers, you can use it to test your sorting code if you wish
def random_list(n=10):
  return [random.randint(0, 100) for i in range(n)]

# This function generates a sorted list of a given size (10 by default). You can use it to test your searching function if you wish
def sorted_list(n=10):
  return sorted(random_list(n))

print([10,12,34,54,56,71,78,82,86,91,93,96])
print(ternary_search([10,12,34,54,56,71,78,82,86,91,93], 95))