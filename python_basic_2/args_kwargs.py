# arguments and keywords
# *args **kwargs

def super_func(*args, **kwargs):
    print(kwargs)
    return sum(args)

super_func(1, 2, 3, 4, 5, num1=5, num2=10)