"""
Program to implement a simple hangman game
"""
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def getGuessedWord(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
     represents which letters in secret_word have been guessed so far.
    """
    word = ""
    for i in secret_word:
        if i in letters_guessed:
            word += i + " "
        else:
            word += "_ "
    return word

def getAvailableLetters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which
     letters have not yet been guessed.
    """
    alpha = ""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            alpha += i
    return alpha

def hangman(secret_word):
    """
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    """
    print("\nWelcome to the game, Hangman!")
    n = str(len(secret_word))
    print("I am thinking of a word that is "  + n + " letters long.")
    guess_left = 6
    letters_guessed = []

    while not isWordGuessed(secret_word, letters_guessed) and guess_left > 0:
        print("- " * 30)
        print("Guesses left: " + str(guess_left))
        print("Available letters:", getAvailableLetters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        while len(guess) > 1:
            guess = input("Please guess a letter: ").lower()
        flag = False
        for i in letters_guessed:
            if guess == i:
                flag = True
                break
        if not flag:
            letters_guessed.append(guess)
        guessed_word = getGuessedWord(secret_word, letters_guessed)
        f = False
        for i in secret_word:
            if i == guess:
                f = True
        if flag:
             print("Oops! You've already guessed that letter:", guessed_word)
        elif f and not flag:
            print("Good guess:", guessed_word)
        else:
            print("Oops! That letter is not in my word:", guessed_word)
            guess_left -= 1

    print("- " * 30)
    if isWordGuessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")

if __name__ == "__main__":
    secretWord = chooseWord(wordlist) #choose word randomly from list
    hangman(secretWord) #call hangman() and start game
