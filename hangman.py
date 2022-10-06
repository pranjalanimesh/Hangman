import random
from os import system
def clear():
   _=system('cls')

import hangies as h
chosen_word = random.choice(h.words)
mod_word = ['_']*len(chosen_word)

game_over=False
death=-1
i=len(chosen_word)

while not game_over:
   x=input("Enter your guess: ").lower()
   clear()
   if x in chosen_word:
      print("Correct!!!")
      for char in range(len(chosen_word)):
         if chosen_word[char]==x :
            print(chosen_word[char],end=' ')
            if(mod_word[char]!=chosen_word[char]):
               mod_word[char]= chosen_word[char]
               i-=1;
         else:
            print(mod_word[char],end=' ')
      print('')
      if i==0:
         print("You Won!")
         game_over=True
   else:
      print("Wrong!!!")
      death+=1
      for char in range(len(chosen_word)):
         print(mod_word[char],end=' ')
      print('')
      print(h.hangman[death])
      print('')
      if death==6:
         print("Game Over! You lose.")
         print(f"The word was {chosen_word}.")
         game_over=True;

input('')
