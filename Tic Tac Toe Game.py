#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
def clear_output():
    os.system('cls')


def display_board(board):
    clear_output()
    print(board[7],"|",board[8],"|",board[9])
    print(board[4],"|",board[5],"|",board[6])
    print(board[1],"|",board[2],"|",board[3])
    


# In[2]:


def player_input():
    marker = ""
    
    while marker != "x" and marker != "o":
        marker = input("Player 1, please choose a marker X or O: ").lower()
    
    player1 = marker
    
    if player1 == "x":
        player2 = "o"
    else:
        player2 = "x"
    return (player1,player2)


# In[3]:


def place_marker(board, marker, position):
    board[position] = marker


# In[4]:


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))


# In[5]:


import random

def choose_first():
    decidefirst = int(input("Guess the number (1 or 2) to start first! "))
    
    while decidefirst >= 3:
        print("This is not a valid option!")
        return choose_first()

        
    if decidefirst == random.randint(1,2):
        return "Player 1"
    else:
        return "Player 2"


# In[6]:


def space_check(board, position):
    return board[position] == " "


# In[7]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[8]:


def player_choice(board):

    
    position = int(input("Choose a position 1-9: "))
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("This position is taken or not valid, choose a position 1-9: "))
    
    return position


# In[9]:


def replay():
    play_again = input("Would you like to play again? Enter Y for yes or N for no: ").lower()
    
    if play_again == "y":
        return True
    elif play_again == "n":
        return False
    else:
        print("This is not a valid option.")
        return replay()


# In[11]:


# the game

print("Welcome to Tic Tac Toe!")
while True:
    game_board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first!")

    play_game = input('Ready to play? y or n: ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1': #Player 1 Turn
            
            display_board(game_board)#show the board
            position = player_choice(game_board)#choose position
            place_marker(game_board,player1_marker,position)
            
            #check if they won 
            if win_check(game_board,player1_marker):
                display_board(game_board)
                print('Player 1 has won!!')
                game_on = False
            #check if its a tie
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('tie game')
                    break
                else:
                    turn = 'Player 2' #no tie and no win  next player turn
        else:
             #show the board  # Player2's turn.
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player2_marker,position)
            
            #check if they won 
            if win_check(game_board,player2_marker):
                display_board(game_board)
                print('Player 2 has won!!')
                game_on = False
            #check if its a tie
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('tie game')
                    break
                else:
                    turn = 'Player 1' #no tie and no win  next player turn
            
            
#if not replay():
    if not replay():
        break
    


# In[ ]:





# In[ ]:




