import math
def what_century(year):
    return str(math.floor(year/100) + 1) + "th"

print(what_century(1999))