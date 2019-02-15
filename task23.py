def ipreq():
    mopen = open("access.log","r")
    firefox = []
    chrome = []
    x = []
    for mop in mopen:
        if "Firefox/" in mop:
            firefox.append(mop)
        elif "Chrome/" in mop:
            chrome.append(mop)
        else:
            x.append(mop)
    print("No of request per browser:")
    print("Firefox",len(firefox))
    print("Chrome",len(chrome))
    print("x",len(x))

ipreq()
