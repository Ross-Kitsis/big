import string
import random
import common
from common import wordProcess


ALLCHARACTERS = list(string.ascii_lowercase[:27])
ADDCHAR = [',' , '.', ';' ,':', '?','!',')','(', '-', "\'", "\"", "@", "#", " " ]
ALLCHAR = ALLCHARACTERS +ADDCHAR
DICTIONARYLOCATION="wordList.txt"

com = wordProcess(DICTIONARYLOCATION,ALLCHAR)

""" Create a random string """
length = 1000000
string = com.create_String(length)

""" Find words in the string"""
foundWords = com.find_Words(string)


print (foundWords)

withDup, withoutDup = com.get_statistics(string,foundWords)

print("Percent with duplicates {}%, Percent without duplicates {}% ".format(withDup, withoutDup))