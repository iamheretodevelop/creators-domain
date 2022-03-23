def is_palindrome(string):
    concatenated_string = ""
    length = len(string)
    for i in range(length):
        if string[i]== " ":
            concatenated_string = concatenated_string + ""
        else:
            concatenated_string = concatenated_string + string[i]
    
    for k in range(len(concatenated_string)):
        if concatenated_string[k] == concatenated_string[::-1]:
            return True
        else:
            return False


    


    