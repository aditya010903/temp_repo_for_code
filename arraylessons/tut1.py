# printing the pair of elements that sum to the target value.
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
target = int(input("Enter the target value:"))

found_pair = False
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        arr[i]= arr[i] + arr[j]
        if arr[i] == target:
            print(f"({i+1}, {j+1})")
            found_pair = True
        elif arr[i] > target:
            break

if not found_pair:
    print("No pair found that sums to the target value.")