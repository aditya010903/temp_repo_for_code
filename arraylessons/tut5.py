def get_array():
    arr = []
    while len(arr) < 6:
        try:
            num = int(input(f"Enter integer {len(arr) + 1}: "))
            arr.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return arr

def max_subarray_sum(arr):
    max_current = max_global = arr[0] 
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

arr = get_array()
arr.sort()
print("Sorted array:", arr)

max_sum = max_subarray_sum(arr)
print("Maximum sum of a subarray:", max_sum)