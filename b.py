import random
import a





a = ['a']*2043
b = ['b']*410
c = ['c']*584
d = ['d']*1099
e = ['e']*3277
f = ['f']*629
g = ['g']*478
h = ['h']*1773
i = ['i']*1736
j = ['j']*34
k = ['k']*255
l = ['l']*1238
m = ['m']*889
n = ['n']*1741
o = ['o']*2578
p = ['p']*433
q = ['q']*27
r = ['r']*1593
s = ['s']*1856
t = ['t']*2557
u = ['u']*1014
v = ['v']*309
w = ['w']*716
x = ['x']*21
y = ['y']*783
z = ['z']*14
dot = ['.']*203
spc = [' ']*6934

DICTIONARYLOCATION="wordList.txt"


def create_dictionary(dictFile):
    """ Read Dictionary file"""
    with open(dictFile) as f:
        words = [x.strip('\n') for x in f.readlines()]
    return words

def find_words(string, dictionary):
    """ Try to find words in the passed String"""
    string = string.split()
    
    allWords = []
    
    for word in string:
        if word in dictionary and len(word) > 1:
            allWords.append(word)        
    
    return allWords

def create_String(length,distribution):
    """ Create a string of the specified length"""
    newString=[None] * length
    for i in range(0,length):
        """Add a letter to the string; uniform distribution"""
        newString[i] = distribution[random.randint(0,len(distribution) - 1)]
    return newString

"""Merge all lists to get the desired distribution, shuffle it??"""
text = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+dot+spc
length = 1000000
random.shuffle(text)

genTest = create_String(length,text)
generated = ''.join(genTest)

dict = create_dictionary(DICTIONARYLOCATION)
found = find_words(generated, dict)
print(found)


