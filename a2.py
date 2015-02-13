import string
import random
import common
from common import wordProcess


ALLCHARACTERS = list(string.ascii_lowercase[:27])
ADDCHAR = [',' , '.', ';' ,':', '?','!',')','(', '-', "\'", "\"", "@", "#", " " ]
ALLCHAR = ALLCHARACTERS +ADDCHAR
DICTIONARYLOCATION="wordList.txt"

com = wordProcess(DICTIONARYLOCATION,ALLCHAR)
string = com.create_String(1000000)
words = com.find_Words(string)


print (words)