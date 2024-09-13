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

# List methods append and extend
print(len(matrix))
print(len(li))
new_li = li.append(100)
new_li = li
print(new_li)

new_li2 = new_li.insert(5, 100)
new_li2 = new_li.insert(2, 100)
new_li2 = new_li.extend([100])
new_li2 = new_li


# removing element using pop 
new_li2.pop(3)
print(new_li2)

# clear
new_li2 = new_li2.clear()
print(new_li2)