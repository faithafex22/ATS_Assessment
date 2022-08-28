#Write a program that takes a text and returns each unique word and the number 
#of times each unique word occurs in that text.
from collections import Counter
def operation(text):
    word_list = text.split()
    c = Counter(word_list)
    print(f'{"word":>5}  {"count":>14}'  )
    for k,v in c.items():
        print(f'{k:>6}  {v:>11}')


operation("twinkle twinkle little star")
    