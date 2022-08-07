def find_it(seq):
    d = {}
    for item in seq:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    for item in d:
        if d[item] % 2 != 0:
            return item

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))