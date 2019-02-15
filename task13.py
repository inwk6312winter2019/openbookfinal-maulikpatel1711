from collections import Dict
import operator
def sorted_words(Book):
    mylist = dict()
    mopen = open(Book,"r")
    for m in mopen:
        m = m.strip()
        m = m.split()
        for r in m:
            if r not in mylist:
                mylist[r] = len(r)

    sorted_a = sorted(mylist.items(), key=operator.itemget(1), reverse = True)
    return sorted_a

b = input("Enter book title:")
print("Output is:", sorted_words(b))
