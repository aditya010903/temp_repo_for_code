# finding the resultant array after rotating an array 'd' times.
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

def array_rotation():
    d = int(input(" Enter the number of roatations of the array:"))
    for i in range(d):
        arr.append(arr.pop(0))
    print("The array after {} rotations is : {}" .format(d,arr))

array_rotation()