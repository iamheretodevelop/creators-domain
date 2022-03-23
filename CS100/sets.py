def find_treasure(treasure, stuff):
    set_a = set(treasure)
    print(set_a)
    count = 0
    for i in stuff:
        if i in set_a:
            count += 1
    return count

a = find_treasure('abAB', 'aBcDeFeDcBa')
print(a)