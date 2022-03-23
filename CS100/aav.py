# def reverse_list(lst):
#     length = len(lst) - 1 
#     for i in range(len(lst)//2):
#         lst[i], lst[length-i] = lst[length-i], lst[i]
#     print(lst)

# lst = [1, 2, 3, -1]
# reverse_list(lst)

words = ["cool", "lock", "cook"]
lst = []
short = len(words[0])
shortest = words[0]
for i in words:
    if len(i) < short:
        short = len(i)
        shortest = i


for i in range(short):
    is_present = True
    for j in range(len(words)):
        word = words[j]
        letter = shortest[i]
        if letter in words[j]:
            words[j] = word.replace(shortest[i], "", 1)
        else:
            words[j] = word.replace(shortest[i], "", 1)
            is_present = False
    if is_present:
        lst.append(letter)

print(lst)



