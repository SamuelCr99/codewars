import math
def what_century(year):
    return str(math.floor(year/100) + 1) + "th"
s = "hello"
s[0] = "k"
print(s)