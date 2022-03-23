import math
# Write a function that takes in two parameters, x, and n, and returns the sum of all multiples of x up to 
# and including n. So if we had x=2 and n = 3, the answer would be 2*1 + 2*2 + 2*3 = 12.

# def money_transfer(dollars, day, exchange_rates):
#     amount_one = dollars * exchange_rates[day-1][1]
#     amount_two = (dollars * exchange_rates[day-1][0]) * 1.6
#     if amount_one > amount_two:
#         print("USA -> Nepal will have maximum profit")
#     else:
#         print("USA -> India -> Nepal will have maximum profit")

# money_transfer(100, 1, [(74.76, 119.22), (71.88, 116.20)])
# print("It\'s still raining")
# print(math.inf)

# a = "Shee sheells sea"
# print(a.split('ee')[-1].split('e'))

# for i in range(0, 6, -1):
#     print(i)

# print([0 for i in range(10)])
def expensive_functions(prices):
    more_than_five = []
    for key, value in prices.items():
        if value > 5:
            more_than_five.append(key)
    return more_than_five

prices = {'mango': 9, 'apple': 4, 'banana': 6}
print(expensive_functions(prices))

def my_function(param1, param2, **arbits):
    print(param1)
    print(param2)
    print(arbits)
# my_function(('a', 'b', 'hi':'hello', 'hello': 'hi', 'bye':'ola')))

