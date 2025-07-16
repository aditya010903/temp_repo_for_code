# finding the smallest positive missng nummber in an array.
def get_array():
    n = int(input("Enter the number of elements in the array:"))
    arr = []
    while len(arr) < n:
        try:
            num = int(input(f"Enter integer {len(arr) + 1}: "))
            arr.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return arr

arr = get_array()

def smallest_positive_missing(arr):
    arr = [num for num in arr if num > 0]
    arr.sort()
    smallest_missing = 1
    for num in arr:
        if num == smallest_missing:
            smallest_missing += 1
    print(f"The smallest positive missing number is {smallest_missing}")

smallest_positive_missing(arr)