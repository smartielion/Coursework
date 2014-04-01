#Casey Gilray
#Assignment #6: Ceaser Cipher
#Date last edited: 10/19/11

def encipher(s,n):
    '''This functuion creates a new encoded string by shifing all letters of s(string)
    to the right n number of letters'''
    #Shift letter with list comprehension
    newS = [letterShift(c,n) for c in s]
    #Concatenate characters into single string
    newloopS = ''
    
    for c in range(len(s)):
        newloopS += newS[c]
    
    return newloopS
    
    
def letterShift(c,n):
    '''This function shifts a single char c to the right N number of letters'''
    #Lowercase
    if ('a' <= c <= 'z'):
        c = ord(c) + n
        #Wrapping
        if c > ord('z'):
            return chr(c-ord('z')+ord('a')-1)
        else:
            return chr(c)
        #Uppercase
    elif ('A' <= c <= 'Z'):
        c = ord(c)+n
        #Wrapping
        if c > ord('Z'):
            return chr(c-ord('Z')+ord('A')-1)
        else:
            return chr(c)
    else:
        #Non-Alphabet, return the character unmoved
        return c

def decipher(s):
    '''This function deciphers any given string based on 3 methods
    The first and highest priority is the letter probability function.
    The second is the english word contents, searching strings for popular english words.
    Last will be the Vowel count of the string.
    '''
    #First level decipher, letter proailility
    listPoss = [(score(encipher(s,n)),encipher(s,n)) for n in range(26)]
    lettProbGuess = max(listPoss)
    #second level decipher, Common word count
    listPoss = [(commCount(encipher(s,n)),encipher(s,n)) for n in range(26)]
    commNumGuess = max(listPoss)
    #thrid level decipher, vowel count
    listPoss = [(numVowel(encipher(s,n)),encipher(s,n)) for n in range(26)]
    vowNumGuess = max(listPoss)
    #find if any of the geusses match, and display that as the "best geuss"
    if lettProbGuess[1] == commNumGuess[1]:
        print('My best guess is: ' + lettProbGuess[1])
    elif lettProbGuess[1] == vowNumGuess[1]:
        print('My best guess is: ' + lettProbGuess[1])
    elif vowNumGuess[1] == commNumGuess[1]:
        print('My best Guess is ' +  vowNumGuess[1])
    else:
        print('My best guess is: ' + lettProbGuess[1])
    return 

def commCount(s):
    '''Counts number of common english words from list on wikipedia
    http://en.wikipedia.org/wiki/Most_common_words_in_English'''
    x = 0
    if 'the' in s: x += 1
    if 'and' in s: x += 1
    if 'to' in s: x += 1
    if 'of' in s: x += 1
    if 'in' in s: x += 1
    if 'that' in s: x += 1
    if 'have' in s: x += 1
    if 'it' in s: x += 1
    if 'for' in s: x += 1
    if 'not' in s: x += 1
    if 'on' in s: x += 1
    if 'with' in s: x += 1
    if 'for' in s: x += 1
    if 'as' in s: x += 1
    if 'do' in s: x += 1
    if 'at' in s: x += 1
    if 'by' in s: x += 1
    if 'we' in s: x += 1
    if 'or' in s: x += 1
    if 'an' in s: x += 1
    if 'so' in s: x += 1
    if 'if' in s: x += 1
    return x

def numVowel(s):
    '''Counts the number of vowels in a string'''
    x = [(c in 'aeiou') for c in s]
    return sum(x)
    
    
def score(s):
    '''Scores a word based on the letter probability scale'''
    wordscore = 1
    for n in range(len(s)):
        wordscore = wordscore * letProb(s[n])
    return wordscore
        

#Table of probabilities for each letter
def letProb(c):
    """ if c is the space character or an alphabetic character,
we return its monogram probability (for english), otherwise we return 1.0 We ignore capitalization. Adapted from http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en
_stat.html
"""
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == c == 'z' or c == 'Z': return 0.0005
    return 1
    