# Learning tuple in python
# they are immutable
my_tuple = (1, 2, 3, 4, 5, 5)
# my_tuple[1] = 'z' this can not be done in a tuple
print(5 in my_tuple)

# faster than a list
# geographic location can use a tuple
# tuple can be a vaid key in a dictionary
# semilar to a list
new_tuple = my_tuple[1:3]
print(new_tuple)

print(my_tuple.count(5))