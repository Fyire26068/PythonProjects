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
a = ' ' #creating letter bank
b = ' '
c = ' '
d = ' '
e = ' '
f = ' '
g = ' '
h = ' '
i = ' '
j = ' '
k = ' '
l = ' '
m = ' '
n = ' '
o = ' '
p = ' '
q = ' '
r = ' '
s = ' '
t = ' '
u = ' '
v = ' '
w = ' '
x = ' '
y = ' '
z = ' '

#wordBank = ["STRING", "ARRAY", "INTEGER", "FLOAT", "PYTHON", "PROGRAM", "CODE", "KEYBOARD", "TYPE", "MOUSE", "COMPUTER", "CHARACTOR", "MONITOR",
            #"GOOGLE", "WHILE", "LOOP", "FOR", "OR", "AND", "DISPLAY", "PRINT", "LOGIC"]#word bank
word = "TESTAAR"
wrong = 0
hangmanDisplay = hangman[wrong]
#word = random.choice(wordBank)
wordLen = len(word)
blanks = '-' * wordLen
wordDisplay =  list(blanks)
startingPos = 0
startCharPos = -1

#initLetterBank = letterBank
print(word)



while hangmanDisplay != hangman[6]: #logic for guess
    charPos = -1
    letterBank = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    #etterBank = initLetterBank
    print(hangmanDisplay)
    print("Word: " + str(wordDisplay))
    print(letterBank)
    guess = input("Guess a Letter : ")
    
    if(guess == 'a' or guess == 'A') and (a != 'A'):#letter A logic
        a = 'A'
        if 'A' not in word:#updating hangman to next level
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]           
        else:#updating current word display
            for i in range(startingPos, wordLen):
                charPos = word.find('A', charPos+1)               
                wordDisplay[charPos] = 'A'
            if word[wordLen - 1] !=  'A' and wordDisplay[wordLen - 1] == 'A':
                wordDisplay[wordLen -1] = "-"
                print(wordDisplay[wordLen - 1])
                
    elif(guess == 'b' or guess == 'B')and (b != 'B'):#letter B logic
        b = 'B'
        if 'B' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('B', charPos+1)                
                wordDisplay[charPos] = 'B'
            if word[wordLen - 1] !=  'B' and wordDisplay[wordLen - 1] == 'B':
                wordDisplay[wordLen -1] = "-"
                
    elif(guess == 'c' or guess == 'C') and (c != 'C'):#letter C logic
        c = 'C'
        if 'C' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('C', charPos+1)                
                wordDisplay[charPos] = 'C'
            if word[wordLen - 1] !=  'C' and wordDisplay[wordLen - 1] == 'C':
                wordDisplay[wordLen -1] = "-"
                
    elif(guess == 'd' or guess == 'D') and (d != 'D'):#letter D logic
        d = 'D'
        if 'D' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('D', charPos+1)                
                wordDisplay[charPos] = 'D'
            if word[wordLen - 1] !=  'D' and wordDisplay[wordLen - 1] == 'D':
                wordDisplay[wordLen -1] = "-"
                
    elif(guess == 'e' or guess == 'E') and (e != 'E'):#letter E logic
        e = 'E'
        if 'E' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('E', charPos+1)                
                wordDisplay[charPos] = 'E'
            if word[wordLen - 1] !=  'E' and wordDisplay[wordLen - 1] == 'E':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'f' or guess == 'F') and (f != 'F'):#letter F logic
        f = 'F'
        if 'F' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('F', charPos+1)                
                wordDisplay[charPos] = 'F'
            if word[wordLen - 1] !=  'F' and wordDisplay[wordLen - 1] == 'F':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'g' or guess == 'G') and (g != 'G'):#letter G logic
        g = 'G'
        if 'G' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('G', charPos+1)                
                wordDisplay[charPos] = 'G'
            if word[wordLen - 1] !=  'G' and wordDisplay[wordLen - 1] == 'G':
                wordDisplay[wordLen -1] = "-"
                
    elif(guess == 'h' or guess == 'H') and (h != 'H'):#letter H logic
        h = 'H'
        if 'H' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('H', charPos+1)                
                wordDisplay[charPos] = 'H'
            if word[wordLen - 1] !=  'H' and wordDisplay[wordLen - 1] == 'H':
                wordDisplay[wordLen -1] = "-"
                
    elif(guess == 'i' or guess == 'I') and (h != 'I'):#letter H logic
        h = 'I'
        if 'I' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('I', charPos+1)                
                wordDisplay[charPos] = 'I'
            if word[wordLen - 1] !=  'I' and wordDisplay[wordLen - 1] == 'I':
                wordDisplay[wordLen -1] = "-"
                
    elif(guess == 'j' or guess == 'J') and (j != 'J'):#letter J logic
        j = 'J'
        if 'J' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('J', charPos+1)                
                wordDisplay[charPos] = 'J'
            if word[wordLen - 1] !=  'J' and wordDisplay[wordLen - 1] == 'J':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'k' or guess == 'K') and (k != 'K'):#letter K logic
        k = 'K'
        if 'K' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('K', charPos+1)                
                wordDisplay[charPos] = 'K'
            if word[wordLen - 1] !=  'K' and wordDisplay[wordLen - 1] == 'K':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'l' or guess == 'L') and (l != 'L'):#letter L logic
        l = 'L'
        if 'L' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('L', charPos+1)                
                wordDisplay[charPos] = 'L'
            if word[wordLen - 1] !=  'L' and wordDisplay[wordLen - 1] == 'L':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'm' or guess == 'M') and (m != 'M'):#letter M logic
        m = 'M'
        if 'M' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('M', charPos+1)                
                wordDisplay[charPos] = 'M'
            if word[wordLen - 1] !=  'M' and wordDisplay[wordLen - 1] == 'M':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'n' or guess == 'N') and (n != 'N'):#letter N logic
        n = 'N'
        if 'N' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('N', charPos+1)                
                wordDisplay[charPos] = 'N'
            if word[wordLen - 1] !=  'N' and wordDisplay[wordLen - 1] == 'N':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'o' or guess == 'O') and (o != 'O'):#letter O logic
        o = 'O'
        if 'O' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('O', charPos+1)                
                wordDisplay[charPos] = 'O'
            if word[wordLen - 1] !=  'O' and wordDisplay[wordLen - 1] == 'O':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'p' or guess == 'P') and (p != 'P'):#letter P logic
        p = 'P'
        if 'P' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('P', charPos+1)                
                wordDisplay[charPos] = 'P'
            if word[wordLen - 1] !=  'P' and wordDisplay[wordLen - 1] == 'P':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'q' or guess == 'Q') and (q != 'Q'):#letter Q logic
        q = 'Q'
        if 'Q' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('Q', charPos+1)                
                wordDisplay[charPos] = 'Q'
            if word[wordLen - 1] !=  'Q' and wordDisplay[wordLen - 1] == 'Q':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'r' or guess == 'R') and (r != 'R'):#letter R logic
        r = 'R'
        if 'R' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('R', charPos+1)                
                wordDisplay[charPos] = 'R'
            if word[wordLen - 1] !=  'R' and wordDisplay[wordLen - 1] == 'R':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 's' or guess == 'S') and (s != 'S'):#letter S logic
        s = 'S'
        if 'S' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('S', charPos+1)                
                wordDisplay[charPos] = 'S'
            if word[wordLen - 1] !=  'S' and wordDisplay[wordLen - 1] == 'S':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 't' or guess == 'T') and (t != 'T'):#letter T logic
        t = 'T'
        if 'T' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('T', charPos+1)                
                wordDisplay[charPos] = 'T'
            if word[wordLen - 1] !=  'T' and wordDisplay[wordLen - 1] == 'T':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'u' or guess == 'U') and (u != 'U'):#letter U logic
        u = 'U'
        if 'U' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('U', charPos+1)                
                wordDisplay[charPos] = 'U'
            if word[wordLen - 1] !=  'U' and wordDisplay[wordLen - 1] == 'U':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'v' or guess == 'V') and (v != 'V'):#letter V logic
        v = 'V'
        if 'V' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('V', charPos+1)                
                wordDisplay[charPos] = 'V'
            if word[wordLen - 1] !=  'V' and wordDisplay[wordLen - 1] == 'V':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'w' or guess == 'W') and (w != 'W'):#letter W logic
        w = 'W'
        if 'W' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('W', charPos+1)                
                wordDisplay[charPos] = 'W'
            if word[wordLen - 1] !=  'W' and wordDisplay[wordLen - 1] == 'W':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'x' or guess == 'X') and (x != 'X'):#letter X logic
        x = 'X'
        if 'X' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('X', charPos+1)                
                wordDisplay[charPos] = 'X'
            if word[wordLen - 1] !=  'X' and wordDisplay[wordLen - 1] == 'X':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'y' or guess == 'Y') and (y != 'Y'):#letter Y logic
        y = 'Y'
        if 'Y' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('Y', charPos+1)                
                wordDisplay[charPos] = 'Y'
            if word[wordLen - 1] !=  'Y' and wordDisplay[wordLen - 1] == 'Y':
                wordDisplay[wordLen -1] = "-"
    elif(guess == 'z' or guess == 'Z') and (z != 'Z'):#letter Z logic
        z = 'Z'
        if 'Z' not in word:
            wrong = wrong +1
            hangmanDisplay = hangman[wrong]
        else:
            for i in range(startingPos, wordLen):
                charPos = word.find('Z', charPos+1)                
                wordDisplay[charPos] = 'Z'
            if word[wordLen - 1] !=  'Z' and wordDisplay[wordLen - 1] == 'Z':
                wordDisplay[wordLen -1] = "-"
    else:
        print('INVALID RESPONSE')
    if '-' not in wordDisplay:#win screen
        print(hangmanDisplay)
        print(wordDisplay)
        print("You guessed the word!\nYou win!")
        break
if hangmanDisplay == hangman[6]:#loss screen
    print(hangmanDisplay)
    print("You lost, the word was " + word)
input()
