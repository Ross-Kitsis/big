import string
import random

ALLCHARACTERS = list(string.ascii_lowercase[:27])
ADDCHAR = [',' , '.', ';' ,':', '?','!',')','(', 
           '-', "\'", "\"", "@", "#", " " ]
ALLCHAR = ALLCHARACTERS +ADDCHAR
DICTIONARYLOCATION="wordList.txt"


def create_dictionary(dictFile):
    """ Read Dictionary file"""
    with open(dictFile) as f:
        words = [x.strip('\n') for x in f.readlines()]
    return words

def create_String(length):
    """ Create a string of the specified length"""
    newString=[None] * length
    for i in range(0,length):
        """Add a letter to the string; uniform distribution"""
        newString[i] = ALLCHAR[random.randint(0,39)]
    return newString

def find_words(string, dictionary):
    """ Try to find words in the passed String"""
    string = string.split()
    
    allWords = []
    
    for word in string:
        if word in dictionary and len(word) > 1:
            allWords.append(word)        
    
    return allWords

def get_statistics(generated, numChar):
    """ List with no duplicate words"""
    noDup = list(set(generated)) 
    noDupChar = len(''.join(noDup)) 
    
    """Get num letters with duplicates"""
    dupChar = len(''.join(generated))
    
    pDupChar = float(dupChar)/numChar * 100
    pChar = float(dupChar)/numChar * 100
    
    print (pDupChar)
    print (pChar)

""" Create the dictionary""" 
DICTIONARY = create_dictionary(DICTIONARYLOCATION)

""" Generate a random String"""
""" length = int(input("Enter the number of characters to test: \n")) """

length = 2000000
print("Generating string with {} characters".format(length))
x = create_String(length)
genString = ''.join(x)

"""Search string for words"""
genWords = find_words(genString, DICTIONARY)
print(genWords)

""" Calculate Word Statistics """
get_statistics(genWords, length)
