# Learning dictionary
dictionary = {
    'a':1,
    'b': 2
}

print(dictionary['b'])
# print(dictionary['c'])
print(dictionary)

# a dictionary is unordered data structure
# dictionary has no order
# a key need to be a immutable which means that it can not be changed
# we have to have a unique key
# creating a dictionary using dict(name='john')
user2 = dict(name='john')
print(user2.items())
print(user2)
print(user2.pop('name'))
print(user2)