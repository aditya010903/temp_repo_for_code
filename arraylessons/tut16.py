# checking if a number is a power of 2 or not.
a = int(input("enter an integer:"))

x = 0
while 2**x <= a:
    if 2**x < a:
        x += 1
    elif 2**x == a:
        print("The number is a power of 2 at index : {}" .format(x))
        break
else:
    print("The number is not a power of 2")

