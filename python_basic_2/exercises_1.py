def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
        return max(evens)

print(highest_even([10, 6, 2, 3, 4, 8, 11]))
        