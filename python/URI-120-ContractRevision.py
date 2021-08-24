while True:
    d,n=map(int,input().split())
    d_str=str(d)
    n_str=str(n)
    n_len= len(n_str)
    out=""

    if(n==d==0):
        break
    else:
        out=n_str.replace(d_str,"")
        if(out==""):
            print(0)
        else:
            print(int(out))
