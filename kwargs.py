# Using **kwargs to accept any number of keyword arguments

def my_function(**kid):
    print("His lastname is: " + kid["lname"])

my_function(fname = "Vishnu", lname="jesus")
