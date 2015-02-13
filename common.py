import string
import random

class wordProcess:
    def __init__(self, dictLocation,characters):
        self.dictLocation = dictLocation
        self.characters = characters
        
        """Create the dictionary for future use"""
        
        with open(self.dictLocation) as f:
            self.words = [x.strip('\n') for x in f.readlines()]
        
    def create_String(self,length):
        """Create a new String of the desired length"""
        self.length = length
        newString=[None] * length
        for i in range(0,length):
            """Add a letter to the string; uniform distribution"""
            newString[i] = self.characters[random.randint(0,len(self.characters)-1)]
        
        """ Convert list to a string, then split it to create words"""
        ns = ''.join(newString)
        newString = ns.split()
        
        return newString
    
    def find_Words(self,pString):
        allWords = []
        """ Iterate through each passed possible word; search dictionary list for that word
            if present add to list of confirmed words"""
        for word in pString:
            if word in self.words and len(word) > 1:
                allWords.append(word)        
        return allWords