def different_occurrences_count(items):
    numbers = set(items)
    repeated_number = 0
    items.sort()
    count = 0
    for i in range(1, len(items) + 1):
        if i not in numbers:
            missing_number = i
    for i in items:
        if i == count:
            repeated_number = i
            break
        count = i
    return [repeated_number, missing_number]

print(different_occurrences_count([1, 8, 3, 4, 5, 6, 7, 4]))
print(different_occurrences_count([1, 1]))