while True:
    try:
        s=str(input())
        s_len=len(s)
        o=''
        counter=0
        for j in range(s_len):
            if s[j]==' ':
                o=o+s[j]
                counter+=1
            elif (j+counter)%2==0:
                o=o+s[j].upper()
            else:
                o=o+s[j].lower()
        print(o)
        
    except EOFError:
        break
