# printing the missing element in the array.
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
for i in range(len(arr)):
        if arr[i+1] != arr[i]+1:
            print(f"the missing number is {arr[i]+1}")
            break
        else:
            pass

        