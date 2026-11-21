# we can combine regular paramenters with *args
#     Regular parameter must come before *args

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Aswath", "Rahman", "venila")