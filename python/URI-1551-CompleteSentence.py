def split(word):
    return {char for char in word}
    
n=int(input())
for i in range(n):
    alphabet={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    s=input()
    splitado=split(s)
    inter=splitado.intersection(alphabet)
    if len(inter)==26:
        print('frase completa')
    elif len(inter)>=13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
