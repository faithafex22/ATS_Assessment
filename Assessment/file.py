#Write a program that reads words from a provided text file and returns each unique word, the
# number of times they appear, the line numbers they appear at and whether its a consonant or vowel.
#In addition to above, the program should output the result above to a csv file whose column
#will be word, is consonant or vowel, number of times it appears, slash separate list of the line numbers.

import csv
from collections import Counter
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

with open("C:/Users/FaithOdunayoAdeosun/Documents/ATS_Assessment/Assessment/words.txt", mode="r", encoding="utf8", newline="")as f:
    contents = f.read()
    per_word = contents.split()
    word_count = Counter(per_word)
    print(f'{"word":>5} {"count":>13}')
    for k,v in word_count.items():
        print(f'{k:>6} {v:>10}')
print("")
print("CHECKER")      
for k,v in word_count.items():
    if set(vowels).intersection(k.lower()) and set(consonants).intersection(k.lower()):
        contains = "contains both V and C"
    elif set(vowels).intersection(k.lower()):
        contains = "contains only V"
    elif set(consonants).intersection(k.lower()):
        contains = "contains only C"
    print(f'{k} {contains}')

print("")    
print('LINENUMBER')
with open("C:/Users/FaithOdunayoAdeosun/Documents/ATS_22/Assessment/words.txt", mode="r", encoding="utf8", newline="")as f:   
    lines = f.readlines()
    for k,v in word_count.items(): 
        for number, line in enumerate(lines, 1):
            if k in line: 
                linenum = f'{k} is in line {number}'
                print(linenum)

header = ['word', 'count', 'contains', 'linenumber']
data = [["twinkle", 2 , "both V  and C", [1]],
        ["little", 1, "both V and C", [1]],
        ["star", 1 , "both V and C", [1]],
        ["how", 1 , "both V and C", [2]],
        ["I", 1 , "only V", [2]],
        ["wonder", 1 , "both V and C", [2]],
        ["what", 1 , "both V and C", [2]],
        ["you", 1 , "both V and C", [2]],
        ["are", 1 , "both V and C", [2]],
        ["up", 1 , "both V and C", [3]],
        ["above", 1 , "both V and C", [3]],
        ["the", 2 , "both V and C", [3,4]],
        ["mount", 1 , "both V and C", [3]],
        ["so", 1 , "both V and C", [3]],
        ["high", 1 , "both V and C", [3]],
        ["like", 1 , "both V and C", [4]], 
        ["a", 1 , "only V", [1,2,3,4]],
        ["diamond", 1 , "both V and C", [4]],
        ["in", 1 , "both V and C", [1,4]],
        ["sky", 1 , "only C", [4]]]     
           
          

with open("C:/Users/FaithOdunayoAdeosun/Documents/ATS_22/Assessment/poem.csv", mode="w", encoding="utf8", newline="")as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
       
