
input_string = input("Enter a string: ")
extract = ""
final_string = ""
repitition = 1
a=1
while a < len(input_string):
    if extract == "":
        extract = ""
    if extract == input_string[a]:
        repitition = repitition + 1
        final_string = final_string + extract   
    elif extract != input_string[a]:
        final_string = final_string + extract + str(repitition)
        repitition = 1
        extract = input_string[a]
    a+=1
final_string += extract + str(repitition)
print ("The final output is: ", final_string)
    