# using enumerate in python
for i, char in enumerate('Helloooo'):
    print(i, char)
# it is used once you need an index number for a counter
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is {i}")