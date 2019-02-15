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
    mytuple = tuple(mylist)
    return mytuple

var = input("enter name of book:")
print("Output is:",unique_words(var))

