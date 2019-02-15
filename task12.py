def isinthis(word):
    mylist = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    flag = False
    for chk in mylist:
        if word == chk:
            flag = True
        else:
            flag = False
    return flag

def unique_words(book):
    mylist = []
    f = open(book,"r")
    for m in f:
        m = m.strip()
        m = m.split()
        for r in m:
            if r != "":
                if r not in mylist:

                    mylist.append(r)

    return mylist

def count_the_article(Book):
    list = unique_words(Book)
    for mi in list:
        check = isinthis(mi)
        if check == True:
            if mi not in mydict:
                mydict[li] = 1
            else:
                mydict[li] += 1
    return mydict

var = input("enter name of book:")
print("Output is:",count_the_article(var))
