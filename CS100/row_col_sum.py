def given_sum(lst, val):
    row_number = 0
    col_number = 0
    if len(lst) == 0:
        return 0
    for row in range(len(lst)):
        row_sum = 0
        for col in range(len(lst[0])):
            row_sum += lst[row][col]
        if row_sum == val:
            row_number += row + 1

    for row in range(len(lst[0])):
        col_sum = 0
        for col in range(len(lst)):
            col_sum += lst[col][row]
        if col_sum == val:
            col_number += row + 1
    return row_number + col_number

print(given_sum([[2, 2], [2, 2]], 4))