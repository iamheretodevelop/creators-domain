# def character(string):
#     character_set = {char for char in string}
#     return character_set

# print(character("One week left!"))

# # string = str

# def is_there_x(lst):
#     for i in lst:
#         for j in i:
#             if j == "X":
#                 return True
#     return False

# print(is_there_x([[".", ".", ".", "."], 
#                   [".", ".", ".", "."], 
#                   [".", "", ".", "."], 
#                   [".", ".", ".", "."]]
#                 ))

# a = ['hi', 'hello', 'ola', 'que paso']
# word_index_dict = {i:a[i] for i in range(len(a))}
# print(word_index_dict) 


# def fizz_buzz(x): 
#     return "fizz" if x % 2 == 0 else "buzz"

# print(fizz_buzz(9))


# class Address:
#     def __init__(self, number, street_name):
#         self.number = number
#         self.street_name = street_name
#     def pretty_print(self):
#         print (self.number, self.street_name)

# home = Address(1234, "Main Street")
# home.pretty_print()


# def first_last_same(lst):
#     a = 0
#     for i in range(len(lst)):
#         if lst[a][0] == lst[a][-1]:
#             lst.remove(lst[a])
#         else:
#             a += 1

# items = ['mom', 'stories', 'dad']
# first_last_same(items)
# print(items)


# def prime(num):
#     lst = []
#     for i in range(2, num):
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             lst.append(i)
#     return lst

# def get_primes(lst):
#     num_primes = {}
#     for i in lst:
#         num_primes[i] = prime(i)
#     return num_primes

# result = get_primes([10, 19, 25, 34])
# print(result)


# def substitute(potential_pwd, key_pwd):
#     new_pwd = ""
#     for char in potential_pwd:
#         if char in key_pwd:
#             new_pwd += key_pwd[char]
#         else:
#             new_pwd += char
#     return new_pwd

# pass_symbols = {'h': '4', 'o': '0', 'e': '3', 'i': '1', 'a': '@', 's': '5'}
# a = substitute('this password rocks', pass_symbols)
# print(a)


def trending(num):
    return True if num>= 1000 else False

def trending_count(lst):
    trending_days = 0
    for day in lst:
        if trending(day):
            trending_days += 1
    return trending_days

def most_popular(titles_counts):
    popular_title = ""
    days = 0
    for title in titles_counts:
        if trending_count(titles_counts[title]) >= days:
            days = trending_count(titles_counts[title])
            popular_title = title
    return popular_title

print(most_popular({'Thank U, Next': [995, 1023, 1012, 956, 902, 887, 1822],
              'Without Me': [1632, 1210, 937, 756, 723, 602, 586],
              'High Hopes': [525, 673, 846, 1015, 1191, 984, 970]}))

