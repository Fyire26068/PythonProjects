import random
#Anthony Garrard
#hangman game
#10/20
hangman = ('''
      _________________
      ||            ||
      ||            ||
     _||_           ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',#creating graphics for game
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
      | |           ||
      | |           ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
    //| |           ||
   // | |           ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
    //| |\\\\         ||
   // | | \\\\        ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
    //| |\\\\         ||
   // | | \\\\        ||
     //             ||
    //              ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''

      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (#_#)          ||
    //| |\\\\         ||
   // | | \\\\        ||
     // \\\\          ||
    //   \\\\         ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''')

wordBank = ["STRING", "ARRAY", "INTEGER", "FLOAT", "PYTHON", "PROGRAM", "CODE",
            "KEYBOARD","TYPE", "MOUSE", "COMPUTER", "CHARACTER", "MONITOR",
            "GOOGLE", "WHILE", "LOOP", "FOR", "OR", "AND", "DISPLAY",
            "PRINT", "LOGIC"]#word bank
wrong = 0
hangmanDisplay = hangman[wrong]
word = random.choice(wordBank)
#print(word)
      
wordLen = len(word)
blanks = '-' * wordLen
wordDisplay = list(blanks)
startingPos = 0
letterBank = list('-' * 26)
bankPos = 0

while hangmanDisplay != hangman[6]: #logic for guess
    charPos = -1#resetting character position
    
    print(hangmanDisplay)#printing screen
    print("Word: " + str(wordDisplay))
    print(letterBank)
          
    guess = input("Guess a Letter : ")#getting guess
    guess = guess.upper()
    
    if len(guess) == 1 and guess >= 'A' and guess <= 'Z': #making sure guess is a vailid response
        if guess not in letterBank: #making sure guess has not been guessed before  
            letterBank[bankPos] = guess #adding guess to the letter bank
            bankPos = bankPos +1 #moving the bank position up 1
            if guess in word: #checking if guess is in the word
                for i in range(startingPos,wordLen): #replacing wordDisplay letters with the correctly guessed letters
                    charPos = word.find(guess, charPos+1)
                    if word[charPos] == guess:
                        wordDisplay[charPos] = guess  
            else: #altering hangman display
                wrong = wrong +1
                hangmanDisplay = hangman[wrong]
        else: #if they already guessed the letter
            print("You already guessed that letter")
    else: #if its an invalid response
        print("Invalid Response")
    if '-' not in wordDisplay: #checking for win
        print(hangmanDisplay)
        print("\nYou won, the word was : " + word + "\n")
        break
if hangmanDisplay == hangman[6]: #making sure its a loss
    print(hangmanDisplay)
    print("\nYou lost, the word was : " + word + "\n")
input()