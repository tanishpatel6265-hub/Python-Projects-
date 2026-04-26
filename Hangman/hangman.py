import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
   word = random.choice(words)
   while '-' in word or ' ' in word :
       word = random.choice(word)
   return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) 
    alphabet = set(string.ascii_uppercase) 
    lives = 7
    word_user = set()
    
    while len(word_letter) > 0 and lives > 0:
      print('You have ', lives , 'lives left and the word guess are:' ,''.join(word_user))
      word_list = [letter if letter in word_user else '-' for letter in  word ]
      print(lives_visual_dict[lives])
      print('Current word :' , ' '.join(word_list))

      
      user_letter = input('Enter your word : ').upper()
      if( user_letter in alphabet - word_user):
         word_user.add(user_letter)
         if(user_letter in word_letter):
            word_letter.remove(user_letter)
         else:
            lives -= 1
            print('\nYour letter,', user_letter, 'is not in the word.')
      elif(user_letter in word_user):
         print("you have allready used this ")
      else:
         print("invalid character ")  
    if(lives == 0):
       print(lives_visual_dict[lives])
       print("Sorry you Die Try again , The word was", word)
    else:
        print('YAY! You guessed the word', word, '!!')
   
hangman()

