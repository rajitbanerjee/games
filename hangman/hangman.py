"""
Program to implement a simple hangman game
"""
import random 
WORDLIST_FILENAME = "words.txt" #file containg words

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

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
             False otherwise
    """
    f = 0
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                f += 1
                break
    if f == len(secretWord):
        return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    word = "" #initialise word
    for i in secretWord:
        f = False #resetting f = False after each iteration
        for j in lettersGuessed:
            if i == j:
                f = True #flag = True if word contains a guessed letter
        if f:
            word += i + " " 
        else:
            word += "_" + " "
    return word



def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    import string
    alpha = ""
    for i in string.ascii_lowercase:
        f = True
        for j in lettersGuessed:
            if i == j:
                f = False
        if f:
            alpha += i   
    return alpha
    

def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    """
    print("Welcome to the game, Hangman!")
    n = str(len(secretWord))
    print("I am thinking of a word that is "  + n + " letters long.")
    guess_left = 8
    lettersGuessed = []
  
    while isWordGuessed(secretWord, lettersGuessed) is False and guess_left > 0:
        print("_ " * 15)
        print("You have " + str(guess_left) + " guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()
        flag = False
        for i in lettersGuessed:
            if guess == i:
                flag = True
                break
        if not flag:
            lettersGuessed.append(guess)
        guessed_word = getGuessedWord(secretWord, lettersGuessed)
        f = False
        for i in secretWord:
            if i == guess:
                f = True
        if flag:
             print("Oops! You've already guessed that letter:", guessed_word)
        elif f and not flag:
            print("Good guess:", guessed_word)
        else:
            print("Oops! That letter is not in my word:", guessed_word)
            guess_left -= 1
                
    print("_ " * 15)
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
       
secretWord = chooseWord(wordlist).lower() #choose word randomly from list
hangman(secretWord) #call hangman() and start game
