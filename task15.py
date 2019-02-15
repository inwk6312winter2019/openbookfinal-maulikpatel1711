mydict = dict()
def histogrm(Book):
    mopen = open(Book,"r")
    for m in mopen:
        m = m.strip()
        m = m.split()
        if len(m) != 0:
            for r in m:
                r = r.lower()
                if r[:1] == 'a' or r[:1] == 'e' or r[:1] == 'i' or r[:1] == 'o' or r[:1] == 'u':
                    if r not in mydict:
                         mydict[r] = 1
                    else:
                         mydict[r] += 1
    return mydict

def starts_with_vow():
    book1 = ["Book1.txt","Book2.txt","Book3.txt"]
    for book in book1:
        histogrm(book)
    return mydict

print("output:",starts_with_vow())
