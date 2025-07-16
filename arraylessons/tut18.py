# finding the equilibrium point in an array

def get_array():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    while len(arr) < n:
        try:
            num = int(input(f"Enter integer {len(arr) + 1}: "))
            arr.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return arr

arr = get_array()

def equilibrium_point():
    left_sum=0
    right_sum= sum(arr)
    for i in range(len(arr)):
        right_sum -= arr[i]
        if left_sum == right_sum:
            print("the equilibrium point is at index: {}" .format(i))
        else:
            left_sum += arr[i]

equilibrium_point()
        