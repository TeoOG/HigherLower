from __future__ import print_function
cls = lambda: print("\033c", end='')

import random
from art import logo, vs
from game_data import data

def higher_lower():
  print(logo)

  # To keep tracking user's score
  score = 0
  # Pick a random number from the list for first compare, save it to 
  # a, do the same b
  a = random.choice(data)
  b = random.choice(data)
  # We don't want same stuff to compare, so we check 
  while a == b:
    b = random.choice(data)
  
  # To continue playing
  user_guessed_correct = True 
  while user_guessed_correct:
        
    # Print A
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    
    # Print the vs logo 
    print(vs)
    
    # Print B
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    
    # print(f"A has {a['follower_count']}")
    # print(f"B has {b['follower_count']}")

    followers_a = int(a['follower_count'])
    followers_b = int(b['follower_count'])
    
    # Ask the user to guess who has more followers 
    guess = input("Who has more followers? Type 'A' or 'B': ")
    
    # Check if user's input is correct
    incorrect_input = True
    while incorrect_input:
      # need to be both False for wrong input
      if guess.lower() != "a" and guess.lower() != "b":   
        guess = input("Not valid input. Type 'A' or 'B': ")
      else:
        incorrect_input = False

    cls()
    print(logo)
    
    if (followers_a > followers_b and guess.lower() == "a") or \
      (followers_a < followers_b and guess.lower() == "b"):
      score += 1
      print(f"You're right!!! Current score: {score}")
      a = b
      b = random.choice(data)
      while a == b:
        b = random.choice(data)
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      # We exit the loop and the game
      user_guessed_correct = False
    
higher_lower()  
  
  
  
  
  
  
  
  
  
