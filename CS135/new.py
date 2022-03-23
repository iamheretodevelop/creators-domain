import copy
class AccessModifiers():
  #protectedInstanceVariable = anagram(str1, str2, k) - list of tuples
  #publicInstanceMethod = palindrome - list of strings
  #privateInstanceVariable = list of odd/even integers
    def __init__(self, publicInstanceVariable, protectedInstanceVariable, privateInstanceVariable):
        self.publicInstanceVariable = publicInstanceVariable
        self._protectedInstanceVariable = protectedInstanceVariable
        self.__privateInstanceVariable = privateInstanceVariable

    def __privateInstanceMethod(self):
      for element in self.__privateInstanceVariable:
        if type(element) != int:
          self.__privateInstanceVariable.remove(element)
      odd_nums = odd(self.__privateInstanceVariable)
      even_nums = even(self.__privateInstanceVariable)
      odd_result = 0
      even_result = 0
      for index, num in enumerate(odd_nums):
        if index % 2 == 0:
          odd_result -= num
        else:
          odd_result += num
      for index, num in enumerate(even_nums):
        if index % 2 == 0:
          even_result += num
        else:
          even_result -= num
      return odd_result * even_result

    def publicInstanceMethod(self):
      private_result = self.__privateInstanceMethod()
      protect = copy.deepcopy(self._protectedInstanceVariable)
      public = copy.deepcopy(self.publicInstanceVariable)
      for string_tuple in protect:
        if check_strings(string_tuple) == False:
          self._protectedInstanceVariable.remove(string_tuple)
      for palindrome in public:
        if not check_palindrome(palindrome):
          self.publicInstanceVariable.remove(palindrome)
      return(self.publicInstanceVariable, self._protectedInstanceVariable, private_result)

def check_strings(string_tuple):
  str_1 = string_tuple[0]
  str_2 = string_tuple[1]
  k = string_tuple[2]
  if type(str_1) != str:
    return False
  new_string_1 = ""
  for char in str_1.lower():
    if not (ord(char) < 97 or ord(char) > 122):
      new_string_1 += char
  if type(str_2) != str:
    return False
  new_string_2 = ""
  for char in str_2.lower():
    if not (ord(char) < 97 or ord(char) > 122):
      new_string_2 += char
  if len(new_string_1) - k == len(new_string_2) or len(new_string_2) - k == len(new_string_1):
    return True
  return False
  

def check_palindrome(string):
  if type(string) != str:
    return False
  new_string = ""
  for char in string.lower():
    if not (ord(char) < 97 or ord(char) > 122):
      new_string += char
  palindrome_check = ""
  for letter in new_string[::-1]:
    palindrome_check += letter
  if new_string == palindrome_check:
    return True
  return False

def odd(list_of_int):
  odd_list = []
  for i in list_of_int:
    if i % 2 != 0:
      odd_list.append(i)
  return odd_list

def even(list_of_int):
  even_list = []
  for i in list_of_int:
    if i % 2 == 0:
      even_list.append(i)
  return even_list


publicInstanceVariable = ['determine', 26, 'mom0', 'articulate', 74]
protectedInstanceVariable = [('Leonardo asw Vinci', 'O, Draconhsyebjian devil!', 6), ('Oh, lame sajwyint!', 'The Mona Lisa', 11), ('Tribainia', 'Brijtain', 3), ('Langyeeeypqbden', 'Engsieybfland', 8), ('Madonna of thjeyye Rocks', 'So dark the cncheon of Man', 9)]
privateInstanceVariable = [39, 'glance', 35, 19, 49]
trial_one = AccessModifiers(publicInstanceVariable, protectedInstanceVariable, privateInstanceVariable)
print(trial_one.publicInstanceMethod())



'''
inputs... 
publicInstanceVariable = ['determine', 26, 'mom0', 'articulate', 74]
protectedInstanceVariable = [('Leonardo asw Vinci', 'O, Draconhsyebjian devil!', 6), ('Oh, lame sajwyint!', 'The Mona Lisa', 11), ('Tribainia', 'Brijtain', 3), ('Langyeeeypqbden', 'Engsieybfland', 8), ('Madonna of thjeyye Rocks', 'So dark the cncheon of Man', 9)]
privateInstanceVariable = [39, 'glance', 35, 19, 49]

output...
(['mom0'], [], 0)
'''