#This is a Rock Paper and Scissors game
#implemented using Python Code.

import random

print(''' The rules of the game is as follows : \n
Rock vs Paper ==============> paper wins\n
Rock vs Scissors ===========> Rock wins\n
Paper vs Scissors ==========> Scissors wins ''')

print('''
The user is to select R, P , or S which stands for Rock, Paper, and Scissors\n
respectively.
once the user selects a valid input, the computer takes a turn to play
this will contunue until a a winner emerges, else it is a tie
''')

#The next line of code creates a loop that enables the user and computer
#continue to play

while True:
    #the next line of code stores a list of the valid keys in a list
    keys = ['R', 'P', 'S']
    User_Choice = input('Kindly enter a valid key ( R, P or S) :' )
    #The next block of codes varifies the user input
    while User_Choice not in keys:
        User_Choice = input('enter a valid key !')

    # The next line of codes initializes the value for each moves of the user
    #and stores the value of Rock Paper and Scissors in a variable

    choice_1 = 'Rock'
    choice_2 = 'Paper'
    choice_3 = 'Scissors'
    
    #The next block of code compares the user input with the valid moves
    #and stores the result in a variable
    if (User_Choice == 'R'):
        user_choice = choice_1
    elif (User_Choice == 'P'):
        user_choice = choice_2
    elif (User_Choice == 'S'):
        user_choice = choice_3

    print(f'You have selected {user_choice}')
    print("It is computer's turn : ")

    choice_list = ['Rock', 'Paper', 'Scissors']
    comp_choice = random.choice(choice_list)

    if comp_choice == 'Rock':
        comp_selection = choice_1
    elif comp_choice == 'Paper':
       comp_selection = choice_2
    else:
       comp_selection = choice_3

    print("Computer has selected : " + comp_selection)

    print(user_choice + ' VS ' + comp_selection)

    #The next block of line compares the user input and computer 

    if ((User_Choice == 'R' and comp_choice == 'Paper') or (User_Choice == 'P' and comp_choice == 'Rock')):
         print('Paper wins!')
         result = 'Paper'

    elif ((User_Choice == 'P' and comp_choice == 'Scissors') or (User_Choice == 'S' and comp_choice == 'Paper')):
         print('Scissors wins!')
         result = 'Scissors'

    elif ((User_Choice == 'R' and comp_choice == 'Scissors') or (User_Choice == 'S' and comp_choice == 'Rock')):
         print('Rock wins!')
         result = 'Rock'

    else:
        print ('Draw!')
        result = 'Draw'

    #condition that determines wether a computer or user wins, or draw.

    if (result == user_choice):
        print('User wins!')
    elif (result == comp_selection):
        print('Computer wins!')

    else:
        print('It is a draw')

    print('Thanks for playing')




    
