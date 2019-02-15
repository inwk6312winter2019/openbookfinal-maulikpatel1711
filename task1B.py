import sys
import string
import collections

def stringManipulation(file):
    list1 = []
    l1 = open("Book1.txt",'r')
    l2 = open("Book2.txt", 'r')
    l3 = open("Book3.txt", 'r')

    for word in words:
        word = word.translate(string.maketrans("",""), string.punctuation).lower()
        modifiedWords = modifiedWords + [word]
    return modifiedWords

    print(modifiedwords)


print(stringManipulation())
