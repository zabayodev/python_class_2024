# A list is a form of arrays in other programing
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']

# Data structure
# the way of organizing data in a structure way
print(li[0])

# a list slicing
print(li[0:2])

li[0] = 8
print(li)

#Constructing a matrix using a list
matrix = [
    [1,2,3],
    [2, 4, 6],
    [7, 8 , 9]
    ]
print(matrix)
print(matrix[0][1])

# List methods
print(len(matrix))
print(len(li))
new_li = li.append(100)
new_li = li
print(new_li)

new_li2 = new_li.insert(1, 100)
new_li2 = new_li
print(new_li2)