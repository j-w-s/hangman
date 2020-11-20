#######################
#       ~~~~~~        #
# -- H A N G M A N -- #
#                     #
# ---   AUTHOR:   --- #
# -- WILL SHEPHERD -- #
#       ~~~~~~        #
#  DATE : 11/20/2020  #
#######################
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# functions

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def getWord():
    userWord = input("What is your word? ")
    while not (userWord.isalpha()):
        userWord = input("Oops! Enter a word. ")
    return userWord
# --------------------------------------------------------------------------------
def makeWordList(userWord, lengthOfList):
    wordList = []
    counter = 0
    for i in range(1, lengthOfList+1, 1):
        wordList.append(userWord[counter:i])
        counter += 1
    return wordList
# --------------------------------------------------------------------------------
def makeBlanks(userWord, lengthOfList):
    blankList = []
    for i in range(0, lengthOfList, 1):
        blankList.append(" _ ")
    return blankList
# --------------------------------------------------------------------------------
def getGuess(guessList):
    lengthGuessList = len(guessList)
    continueGuess = "Y"
    while not (continueGuess == "N"):
        letterGuess = input("What is your guess? ")
        while not (letterGuess.isalpha() and len(letterGuess) == 1):
            if not (letterGuess.isalpha()):
                letterGuess = input("Oops! Enter a letter, not a number or other character. ")
            if not (len(letterGuess) == 1):
                letterGuess = input("Oops! Enter a single letter, not multiple numbers, letters, or other characters. ")
        for i in range(0, lengthGuessList, 1):
            if (letterGuess == guessList[i]):
                print("Oops! You already guessed this letter. Try another.")
                continueGuess = "Y"
                break;
            else:
                guessList.append(letterGuess)
                continueGuess = "N"
    return letterGuess, guessList
# --------------------------------------------------------------------------------
def searchForGuess(wordList, blankList, letterGuess, lengthOfList, numberOfFailedAttempts):
    counter = 0
    for i in range(0, lengthOfList, 1):
        if letterGuess == wordList[i]:
            blankList[i] = wordList[i]
        else:
            counter +=1
    if (counter == lengthOfList):
                print("Your guess was not found in the word!")
                numberOfFailedAttempts += 1
    else:
        print("Your guess was found in the word!")
    return blankList, numberOfFailedAttempts
# --------------------------------------------------------------------------------
def displayHangman(blankList, numberOfFailedAttempts):
    if (numberOfFailedAttempts == 0):
        print("_________")
        print("|       |")
        print("|       |")
        print("|       |")
        print("|       |")
        print("|_______|")
    if (numberOfFailedAttempts == 1):
        print("_________")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("|       |")
        print("|_______|")
    if (numberOfFailedAttempts == 2):
        print("_________")
        print("|       |")
        print("|   O   |")
        print("|   |   |")
        print("|       |")
        print("|_______|")
    if (numberOfFailedAttempts == 3):
        print("_________")
        print("|       |")
        print("|   O   |")
        print("|   |\  |")
        print("|       |")
        print("|_______|")
    if (numberOfFailedAttempts == 4):
        print("_________")
        print("|       |")
        print("|   O   |")
        print("|  /|\  |")
        print("|       |")
        print("|_______|")
    if (numberOfFailedAttempts == 5):
        print("_________")
        print("|       |")
        print("|   O   |")
        print("|  /|\  |")
        print("|    \  |")
        print("|_______|")
    if (numberOfFailedAttempts == 6):
        print("_________")
        print("|       |")
        print("|   O   |")
        print("|  /|\  |")
        print("|  / \  |")
        print("|_______|")
    if (numberOfFailedAttempts == 7):
        print("_________")
        print("|   |   |")
        print("|   O   |")
        print("|  /|\  |")
        print("|  / \  |")
        print("|_______|")
    print("\n{}".format(blankList))
# --------------------------------------------------------------------------------
def checkIfMatching(wordList, blankList, lengthOfList):
    counter = 0
    for i in range(0, lengthOfList, 1):
        if (blankList[i] == wordList[i]):
            counter += 1
    if (counter == lengthOfList):
        return "Y"
    else:
        return "N"
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# variables

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
userContinue = "Y"
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#######################
#       ~~~~~~        #
# --- M  A  I  N  --- #
#       ~~~~~~        #
#######################

while (userContinue in ["Y", "y", "YES", "YEs", "Yes", "yes"]):
    failedAttempts = 0
    listOfGuesses = [""]
    gameOver = "N"
    word = getWord()
    wordLength = len(word)
    listOfWords = makeWordList(word, wordLength)
    listOfBlanks = makeBlanks(word, wordLength)
    displayHangman(listOfBlanks, failedAttempts)
    while not (failedAttempts == 8):
        letter, listOfGuesses = getGuess(listOfGuesses)
        listOfBlanks, failedAttempts = searchForGuess(listOfWords, listOfBlanks, letter, wordLength, failedAttempts)
        displayHangman(listOfBlanks, failedAttempts)
        gameOver = checkIfMatching(listOfBlanks, listOfWords, wordLength)
        if (gameOver == "Y"):
            print("You won!")
            break;
        elif (failedAttempts == 7):
            print("You lost!")
            break;
    userContinue = input("Do you want to play again (Y/N)? ")
