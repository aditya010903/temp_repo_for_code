# printing the number of triangles that can be formed from the array.
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
count_triangles = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
       sum= arr[i] + arr[j]
       for k in range(j + 1, len(arr)):
           if sum > arr[k]:
               count_triangles += 1
               print(f"({arr[i]}, {arr[j]}, {arr[k]})")
           else:
               break
print("Number of triangles:", count_triangles)