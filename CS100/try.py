# def count_vowels(items):
#     vowel_list = "aeiou"
#     vowel_counter = 0
#     for row in items:
#         for item in row:
#             if item in vowel_list:
#                 vowel_counter += 1
#     return vowel_counter


def is_prime(num):
    if num < 2: 
        return False 
    if num == 2: 
        return True 
    for i in range(2, int(num**0.5)+1):
        if num % i == 0: 
            return False
    return True 
   
def foo():
    """
    Write a list comprehension in this function to return a list of all primes 
    between 1 to 1000. 
    """
    print([num for num in range(1, 1001) if is_prime(num) == True])

x = foo()