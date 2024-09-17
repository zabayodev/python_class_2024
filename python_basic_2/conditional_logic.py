is_old = False
is_licensed = True

if is_old:
    print('You are old enough to drive')
else:
    print('check your age again!')
    
# Ternary operator
''' it is a conditional logic where all the conditions and if clause are on the same line'''
# condition_if_tru if condition ense condition_if_false

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)