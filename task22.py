import operator
def topip():
    mydict = dict()
    mopen = open("access.log","r")
    for mop in mopen:
        if "GET /" in mop or "POST /" in mop:
            ip = mop.split('-')[0]
            if ip not in mydict:
                mydict[ip] = 1
            else:
                mydict[ip] += 1
    sorted_a = sorted(mydict, key=mydict.get, reverse=True)[:20]
    return sorted_a


print(topip())
