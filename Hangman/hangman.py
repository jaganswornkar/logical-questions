import random
from words import random_word    # random_word() contains a random word from the word list(words.txt)
from images import IMAGES        # IMAGES contains a list of images of hangman according to the levels form images.py

# all predefined details for the game.
lives = 8
random_word = random_word()
word_length = len(random_word)
hangman = ("_ " * word_length).split()
guessed_chars = ''
print(
    "Welcome to the Hangman game (word guessing game)\n",
    "length of word is ",len(hangman)
)


while lives > 0:
    
    print(
        " lives :",lives,'\n',
        'hangman :',(' ').join(hangman),'\n',
        'guessed chars :',guessed_chars,'\n'
    )
    # checking the condition for win(guessed the word)
    if ('').join(hangman) == random_word:
        print(
            "Hurrehhh! You won the game :)"
        )
        break
    # taking user input in single character (to guess the word)
    user = input('guess a character for the word : ')
    user = ((' ').join(user).split()[0])

    # condition to check if the character exists in word, 
    # if exists then it will show in hangman otherwise it will show hangman and decrease the lives of the man
    if user in random_word:
        for i in range(len(random_word)):
            if user == random_word[i]:
                hangman[i] = user
    else:
        img_ind = (len(IMAGES)-(lives+1))
        print('ooops! wrong guess, please try again---\n',IMAGES[img_ind])
        lives -= 1
    guessed_chars += user+' '

# condition for user lost the game (checking if the random word is not equal to the user guessed word)
if ('').join(hangman) != random_word:
    print(
        " lives :",lives,'\n',
        'hangman :',(' ').join(hangman),'\n',
        'guessed chars :',guessed_chars,'\n'
    )
    print(
        "\n Sorry! You loss the game, please try again.\n",
        "your word was : ",random_word
    )
                

    