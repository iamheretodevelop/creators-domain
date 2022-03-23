def sum_numbers(number): 
    sum_number = 0
    sum_digits = ""
    for i in number:
        if i == " ":
            sum_number += int(sum_digits)
            sum_digits = ""
        else:
            sum_digits += i
    sum_number += int(sum_digits)
    return sum_number

print(sum_numbers('123 4 1000 1'))