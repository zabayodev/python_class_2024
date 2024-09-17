# for item in [1, 2, 3, 4, 5]:
#     print(item)
    
    # iterable - list, dictionary, tuple, set, string
    # iterated -> one by one check for each item in the collection.
    # for a dictionary, you print only the keys
    
user = {
        'name': 'Golem',
        'age': 5006,
        'can_swim': False
    }    
    
# for item in user:
#         print(item)    
for item in user.items():
        print(item) 
        
for item in user.values():
        print(item) 
        
for item in user.keys():
        print(item) 