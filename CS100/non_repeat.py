def non_repeat(items):
    """
    The function takes a list of integers and returns the first items that does not repeat itself in the list. 
    The function should return None if there is no such integer. 
    eg: 
    input: lst = [1, 2, 3, 1, 3]
    output: non_repeat(lst) -> 2 
    
    input: lst = [1, 2, 3, 1, 3, 2]
    output: non_repeat(lst) -> None
    """
    if len(items) == 0:
        return None
    for integer in range(0, len(items)):
        val = True
        for check in range(0, len(items)):
            if check == integer:
                continue
            if items[integer] == items[check]:
                val = False
        if val == True:
            return items[integer]
    if val == True:
        return items[len(items) - 1]
    return None

a = non_repeat([-5, 4, 4, 4, -5, -8])
print(a)