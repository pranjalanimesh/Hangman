import os

hangman1= '''    
   _____
   |    |
   O    |
        |
        |
        |
       /_\ 
       '''

hangman2 = '''
    _____
   |    |
   O    |
   |    |
        |
        |
       /_\ 
       '''

hangman3 = '''
    _____
   |    |
   O    |
   |/   |
        |
        |
       /_\ 
       '''

hangman4 = '''
    _____
   |    |
   O    |
  \|/   |
        |
        |
       /_\ 
       '''

hangman5 = '''
    _____
   |    |
   O    |
  \|/   |
   |    |
        |
       /_\ 
       '''

hangman6 = '''
    _____
   |    |
   O    |
  \|/   |
   |    |
    \   |
       /_\ 
       '''

hangman7 = '''
    _____
   |    |
   O    |
  \|/   |
   |    |
  / \   |
       /_\ 
       '''

hangman = [hangman1,hangman2,hangman3,hangman4,hangman5,hangman6,hangman7]

a_file = open(os.path.dirname(__file__)+"\\words.txt", "r+")

lines = a_file.read()
words = lines.splitlines()

a_file.close()

# words = ['apple','banana','camel','daddy','elephant','flamingo']