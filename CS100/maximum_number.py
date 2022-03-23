number_1 = int(input ("Enter a number: "))
number_2 = int(input ("Enter a number: "))
number_3 = int(input ("Enter a number: "))
number_4 = int(input ("Enter a number: "))
number_5 = int(input ("Enter a number: "))
number_6 = int(input ("Enter a number: "))
number_7 = int(input ("Enter a number: "))
number_8 = int(input ("Enter a number: "))
number_9 = int(input ("Enter a number: "))
number_10 = int(input ("Enter a number: "))

inputs = [number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8, number_9, number_10]
largest = 0
for number in inputs:
        if number > largest:
                largest = number
print(f"The maximum number is: {largest}")

