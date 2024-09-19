# using while loop in python
# using an infinite loop
# i = 0
# while 0 < 50:
#     print(i)

# i = 0
# while 0 < 50:
#     print(i)
#     break

i = 0
while i < 50:
    print(i)
    i += 1
    break
else:
    print('Done with all the work')

# when to use a for loop and a while loop
for item in [1, 2, 3]:
    print(item)
    
while True:
    response = input('say something: ')
    if (response == 'bye'):
        break