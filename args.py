
def my_function(*kids):
    print("The youngest child is " + kids[2])
    print("The elder child name is " + kids[1])
# The args parameter allows a fucntion to accept any number of positional arguemnts.
# Inside the function, args become tuple containing all the passed arguments

my_function("Emil", "Banumitha", "malasha")
# print(my_function())