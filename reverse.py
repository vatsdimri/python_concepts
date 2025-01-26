def reverse(s):
    length  = len(s)
    temp = ""
    for i in range(length):
        temp = temp + s[-i-1]
    return temp
s = "what are you saying?"

print(reverse(s))