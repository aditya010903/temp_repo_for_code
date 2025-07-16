# multiple assignments
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# single assignment to multiple variables.
x = y = z = "Orange"
print(x)
print(y)
print(z)


# unpacking a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# global variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


# using local and global variables 
'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)    this gives output as python is fantanstic

myfunc()

print("Python is " + x)      this gives an output as python is aweswome 

'''




