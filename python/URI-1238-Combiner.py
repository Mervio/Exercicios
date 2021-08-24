n=int(input())
for i in range (n):
    a,b=input().split()
    c= max(len(a),len(b))
    o=''
    for i in range (c):
        if i< len(a):
            o=o+a[i]
        if i< len(b):
            o=o+b[i]
    print(o)
    
