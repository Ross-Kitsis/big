import random
import common
from common import wordProcess

""" Create list of characters based on the given distribution, shuffle """
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
ALLCHAR=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+dot+spc
random.shuffle(ALLCHAR)

DICTIONARYLOCATION="wordList.txt"
length = 1000000

com = wordProcess(DICTIONARYLOCATION,ALLCHAR)

""" Create a random string """
string = com.create_String(length)

""" Find words in the string"""
foundWords = com.find_Words(string)

withDup, withoutDup = com.get_statistics(string,foundWords)

print("Percent with duplicates {}%, Percent without duplicates {}% ".format(round(withDup,2), round(withoutDup,2)))





