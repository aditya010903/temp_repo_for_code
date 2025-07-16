# sorting an array containing 0, 1, 2 manually. (without using the sort method)
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

zeros=[]
ones=[]
twos=[]
for i in range(len(arr)):
    if arr[i]==0:
        zeros.append(arr[i])
    elif arr[i]==1:
        ones.append(arr[i])
    else:
        twos.append(arr[i])

arr= zeros+ones+twos
print("Sorted array of 0 , 1, 2 :", arr)