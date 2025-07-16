# printing the Second largest element in the array.

def get_array():
    arr = []
    while len(arr) < 6:
        try:
            num = int(input(f"Enter integer {len(arr) + 1}: "))
            arr.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return arr

arr = get_array()
arr.sort()
print("Sorted array:", arr)
print("the second largest element of the array is {}".format(arr[-2]))