def filtered(input1:list, input2:list, input3:dict, input4:dict):
  even_filter = filter(lambda x:(x % 2 == 0), input1)
  odd_filter = filter(lambda x:(x % 2 != 0), input2)
  even_value_filter = filter(lambda x:(input3[x] % 2 == 0), input3)
  odd_value_filter = filter(lambda x:(input4[x] % 2 != 0), input4)
  sum_filter = sum(list(even_filter) + list(odd_filter))
  return sum_filter, list(even_value_filter) + list(odd_value_filter)

print(filtered([1,8,10], [9,3,4], {'A':1, 'B':2, 'C':3}, {'A':4, 'B':2, 'C':3}))