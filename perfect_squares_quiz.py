#intro
max_root = input("Welcome to the perfect squares quiz! Enter what number you want the roots to go up to: ")

#to ask another question
again = "yes"
while(again == "yes"):

    import random

    #turn max root into int
    max_rootint = int(max_root)

    #get random root number
    root = random.randint(1,max_rootint)

    #ask perfect square
    print("What is", root, "squared: ")
    ans = int(input(""))

    #check if correct
    if(ans == root**2):
        print("Correct")
        #to ask another question
        again = input("Would you like to do another question? Type yes or no, all lower case: ")

    else:
        print("Incorrect! The answer was,", root**2)
        #to ask another question
        again = input("Would you like to do another question? Type yes or no, all lower case: ")

print("Bye!")
