def number_of_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return 1 + number_of_paths(rows-1, columns-1)

print(number_of_paths(3,3))
