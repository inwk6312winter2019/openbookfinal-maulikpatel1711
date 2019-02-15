def mylogs():
    mopen = open("access.log","r")
    mget = open("get.log","w")
    mpost = open("post.log","w")
    mput = open("put.log","w")
    mdelete = open("delete.log","w")
    for mpe in mopen:
        if "GET /" in mpe:
            mget.write(mpe)
        elif "POST /" in mpe:
            mpost.write(mpe)
        elif "PUT /" in mpe:
            mput.write(mpe)
        else:
            mdelete.write(mpe)


mylogs()
