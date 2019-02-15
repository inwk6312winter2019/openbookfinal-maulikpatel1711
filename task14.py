from collections import Dict
import operator
def character_word_count(Book):
    mylist = dict()
    mopen = open(Book,"r")
    for m in mopen:
        m = m.strip()
        m = m.split()
        for r in m:
            if r not in mylist:
                mylist[r] = len(r)
    return mylist

b = input("Enter book title:")
print("Output is:", character_word_count(b))
print("count character words")

