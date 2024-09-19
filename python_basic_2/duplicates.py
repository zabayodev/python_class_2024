my_list = ['a', 'b', 'b', 'c', 'd', 'm', 'n', 'n']
duplicates = []
for value in my_list:
    if my_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)