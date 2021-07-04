"""
For this challenge you will be replacing certain characters in a string.
have the function ASCIIConversion(str) take the str parameter being passed and return a new string where every character,
aside from the space character, is replaced with its corresponding decimal character code. 
For example: if str is "dog" then your program should return the string 100111103 because d = 100, o = 111, g = 103./#
"""
def ascii(s):
    a=len(s)
    result = ""
    for i in range (a):
        b=ord(s[i])
        if b != 32:
            result += str(b)
        else :
            result += " "
    return result

print(ascii("hello world"))