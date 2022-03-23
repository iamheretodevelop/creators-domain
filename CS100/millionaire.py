# Who wants to be a Millionaire??

# The progression in this "short" version of millionaire should be:
# 1 answer correct: $500
# 2 answers correct: $1000
# 3 answers correct: $5000
# 4 answers correct: $20000
# 5 answers correct: $50000
# 6 answers correct: $250000
# 7 answers correct: $500000
# 8 answers correct: $1000000

# Your code here!
player_name = input("Welcome to Millionaire! What is your name? ")
money_made = 0
print (f"Currently you have made ${money_made}.")

#Question 1
for x in range(7):
    print ("What is the capital city of India? \n a. Mumbai \n b. New Delhi \n c. Agra \n d. Kolkata")
    answer_1 = input(">>")
    answer_1 = answer_1.lower()
    if answer_1 == "b":
        print ("Correct!")
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
    money_made += 500
    print (f"Currently you have made ${money_made}.")

#Question 2
    print ("What is the planet nearest to Sun? \n a. Earth \n b. Venus \n c. Mercury \n d. Jupiter")
    answer_2 = input(">>")
    answer_2 = answer_2.lower()
    if answer_2 == "c":
        print ("Correct!")
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
    money_made += 500
    print (f"Currently you have made ${money_made}.")

#Question 3
    print ("Who discovered electrons? \n a. Rutherford \n b. JJ Thompson \n c. Einstein \n d. James Chadwick")
    answer_3 = input(">>")
    answer_3 = answer_3.lower()
    if answer_3 == "b":
        print ("Correct!")
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
    money_made += 4000
    print (f"Currently you have made ${money_made}.")

#Question 4
    print ("Who won the first ever soccer world cup? \n a. Argentina \n b. Uruguay \n c. Brazil \n d. Spain")
    answer_4 = input(">>")
    answer_4 = answer_4.lower()
    if answer_4 == "b":
        print ("Correct!")
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
    money_made += 15000
    print (f"Currently you have made ${money_made}.")

#Question 5
    print ("What is the highest iMDB rated movie? \n a. Shawshank Redemption \n b. Forrest Gump \n c. Godfather I \n d. Dark Knight Rises")
    answer_5 = input(">>")
    answer_5 = answer_5.lower()
    if answer_5 == "a":
        print ("Correct!")
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
    money_made += 30000
    print (f"Currently you have made ${money_made}.")

#Question 6
    print ("Who is the President of the USA? \n a. Donald Trump \n b. Barack Obama \n c. Bernie Sanders \n d. Joe Biden")
    answer_6 = input(">>")
    answer_6 = answer_6.lower()
    if answer_6 == "d":
        print ("Correct!")
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
    money_made += 200000
    print (f"Currently you have made ${money_made}.")

#Question 7
    print ("What is the peak of the world? \n a. Mt. Everest \n b. Mt. Kilimanjaro \n c. Mt. Kanchenjunga \n d. Mt. Gaurishankar")
    answer_7 = input(">>")
    answer_7 = answer_7.lower()
    if answer_7 == "a":
        print ("Correct!")
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
    money_made += 250000
    print (f"Currently you have made ${money_made}.")

#Question 8
    print ("What is the largest source of earth's oxygen? \n a. Trees \n b. Phytoplankton \n c. Minerals \n d. Oxygen plants")
    answer_8 = input(">>")
    answer_8 = answer_8.lower()
    if answer_8 == "b":
        print ("Correct!")
        print ("You are a millionaire!")
        break
    else:
        print ("I'm sorry, that is incorrect")
        print (f"Currently you have made ${money_made}.")
        break
print ("Congratulations,", player_name)

