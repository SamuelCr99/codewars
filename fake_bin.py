def fake_bin(x):
    for i in range(1,5):
        x = x.replace(str(i),"0")
    for i in range(5,10):
        x = x.replace(str(i),"1")
    return x