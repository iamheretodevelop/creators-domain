# lst = ['hello', 'from', 'the', 'other', 'side']
# string = '---'.join(lst)
# print(string)

# for i in range(5,0,-1):
#     print(i)

# def func1(a):
#     def func2():
#         a = 4
#         return a
#     print(a)
#     return func2

# func = func1(5)
# print(func())

# def help(a, b=1, **keyword):
#     print(a)
#     print(b)
#     print(keyword)

# helper = help(1, 2, dict = 1)

# from functools import reduce
# lst = [1, 2, 3, 4, 6, 5]
# reduced = reduce(lambda a,b: a if a>b else b,lst)
# print(reduced)

# lst1 = [1, 2, 3, 4, 5]
# mapped = map(lambda x:x**2, lst1)
# print(list(mapped))

# lst2 = [3, 4, 6, 9, 10, 9]
# filtered = filter(lambda x : x % 3 == 0, lst2)
# print(tuple(filtered))

# def func(*arg):
#     total = 0
#     for number in arg:
#         total += number
#     return total
# print(func(1, 2, 3, 4))

class Boy:
    sex_organ = "penis"
    def __init__(self, name, grade, password):
        self.name = name
        self.year = grade
        self.__password = password

Harke = Boy("Harke", "Freshman", "helloworld")
print(Harke.__password)

# class Mammal:
#     def __init__(self, type_of):
#         self.type = type_of
#     def give_birth(self):
#         print(self.type + " doesn't lay eggs")
#     def feed_the_young(self):
#         print(self.type + " feeds milk.")

# class Platypus(Mammal):
#     def feed_the_young(self):
#         super().feed_the_young()
#         print("But, the milk is produced as belly sweat!!")

# platy = Platypus("Platypus")
# print(platy)
# platy.feed_the_young
# dog = Mammal("Dog")
# dog.give_birth()
# print(isinstance(dog, Mammal))

# def outer(a):
#     print("Outer a:", a)
#     def inner():
#         a = 10
#         return a
#     return inner

# a = 100
# first_call = outer(a)
# print(first_call())