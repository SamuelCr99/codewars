def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    upp = 0
    side = 0
    for dir in walk:
        if dir == "n":
            upp += 1
        if dir == "s":
            upp -= 1 
        if dir == "e":
            side += 1
        if dir == "w":
            side -= 1 
    if upp == 0 and side == 0:
        return True
    return False

                
            
