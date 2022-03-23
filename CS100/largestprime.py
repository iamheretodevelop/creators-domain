
#Asking for a user input. 
num = int(input("Enter a number: "))

# The program should find the largest prime number less than num. 
prime = None
# Your code. 

for i in range(2, num):
    j = 2
    is_prime = True
    while j<=i:
        if i!=j and i % j == 0:
            is_prime = False
            break
        else:
            j += 1
    if is_prime:
        prime = i

print("The number is", prime)