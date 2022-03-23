string = ""
keep_going = True
while keep_going == True:
    user_char = input("Enter a character (or 'stop' to stop): ")
    if user_char == "stop" :
        keep_going = False
    elif len(user_char) != 1:
        print("Must provide only single character. Try again.")
    else: 
        string = string + user_char
print("The full string is", string)