# python-by-Hiren-Gediya
#fully start-up based
import random

computer_choice = int(random.choice([-1, 0, 1]))

user_input = int(input("Enter your choice : "))

print(f"your choice is {user_input}")
print(f"computer choice is {computer_choice}") 

""" 
-1 = s     -1 = 0 win   /////    -1 = 1 win //////////   0 = -1 loss    ////   0 = 1 win   ///////  1 = -1   loss  ////   1 = 0 loss
0 = w
1 = g
"""
if(user_input not in [-1, 0, 1]):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!please change value and retry!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    if (computer_choice == user_input):
        print("tie")
    else:
        if(user_input == -1 and computer_choice == 1):
            print("win")
        elif(user_input == -1 and computer_choice == 0):
            print("win")
        elif(user_input == 1 and computer_choice == -1):
            print("loss")
        elif(user_input == 1 and computer_choice == 0):
            print("loss")
        elif(user_input == 0 and computer_choice == 1):
            print("win")
        elif(user_input == 0 and computer_choice == -1):
            print("loss")
        else:
            print("something wrong with this step!")
