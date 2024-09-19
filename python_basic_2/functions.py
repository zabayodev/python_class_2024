# Developing functions in python
# using DRY(Do not Repeat Yourself)
# def say_hello():
#     print('helloooo')
    
# say_hello()

# parameters and arguments
def say_hello(name='gretta', emoji='$$$'): # parameters in the functions
    print(f'helloooo {name} {emoji}')
    
# Arguments
# positional parameters and argument
say_hello('Emma', '**')
say_hello('Dan', '**')
say_hello('Emily', '**')

# keyword arguments
say_hello(emoji = '&&', name='Bibi')

# Default parameters
say_hello()

# return
def sum(num1, num2):
    return num1 + num2
    
total = sum(10, 6)
print(sum(10, total ))

# function should do one thing really well
# should return something