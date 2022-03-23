# Given a list of numbers, return the second largest in the list.
  
  #first find the largest number in the list
  #then go over each element in the list, and compute them to find the number second largest. 
  
def second_largest_number(list_of_numbers):
  if len(list_of_numbers) == 0:
    return None
  largest_number = max(list_of_numbers)
  second_largest = list_of_numbers[0]
  for number in list_of_numbers:
    if number < largest_number and number > second_largest:
      second_largest = number
  return second_largest

print(second_largest_number([1, 2, 3, 4, 5, 100, 101]))
    
#Runtime complexity = O(n)

# ----

# Given two strings of digits, return the string that corresponds to a larger number when the digits are sorted in decreasing order.

# Input1: "3711"  -> 7311
# Input2: "5462"  -> 6542

# Since 7311 > 6542, return "3711"

#let's not assume the lengths of strings are same
#return the value as a string, not an integer
#return None or arbitrary for equal numbers
#return the other if one is empty, or both are empty, return either or None
#validated string of digits only

def larger_decreasing_number(number_one, number_two):
  if len(number_one) == 0 and len(number_two) == 0:
    return None
  elif len(number_two) == 0:
    return number_one
  elif len(number_one) == 0:
    return number_two
  number_one_list = []
  number_two_list = []
  decreasing_number_one = ""
  decreasing_number_two = ""
  for digit in number_one: 
    number_one_list.append(digit)
  for digit in number_two:
    number_two_list.append(digit)
  number_one_list.sort(reverse = True)
  number_two_list.sort(reverse = True)
  for digit in number_one_list:
    decreasing_number_one += digit
  for digit in number_two_list:
    decreasing_number_two += digit
  decreasing_number_one = int(decreasing_number_one)
  decreasing_number_two = int(decreasing_number_two)
  if decreasing_number_one > decreasing_number_two:
    return str(number_one)
  elif decreasing_number_one < decreasing_number_two:
    return str(number_two)
  else:
    return None
  
print(larger_decreasing_number("3711", "1293"))
  #Runtime = O(max(n,m)) where n = len(number_one) and m = len(number_two)