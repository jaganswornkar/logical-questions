import string
import random

# this function helps to load a large number of words and create a list
def load_words():
    word_list = open("words.txt",'r')
    word_list = word_list.read().split()
    return word_list


# this function returns a randomly choosen word from the wordlist
def random_word():
    word_list = load_words()
    rw = random.choice(word_list)
    return rw