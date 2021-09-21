
num_of_tries = 0
num = 10
print(" Welcome to the number guessing game!")

while True:
    #get input
    try:
        guess = int(input("What number am I thinking of? (1-100 or 0 to exit):"))
        num_of_tries +=1
    except:
        print("Please input a number 1-100!")
        continue
    if guess == 0:
        break
    elif guess <1 or guess > 100:
        print("Please input a number 1-100!")
    else:
        if num == guess:
            print("You won!")
            again = input("Would you like to play again? Enter 'Y' for Yes, and anything else for No:")
            if again == 'Y' or again =='y':
               num =10
               num_of_tries = 0
            else:
               break
        else:
            if num > guess:
                print(" Too loww, try again.")
            else:
                print("Too high, try again.")
print("Thanks for playing, and we hope to see u again")    
    


