# printing the number of distinct elements in each window of size k.
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
arr.sort()
print("Sorted array:", arr)

def distinct_window(arr, k):
    distinct_counts = []
    for i in range(len(arr) - k + 1):
        window = arr[i:i + k]
        distinct_count = len(set(window))
        distinct_counts.append(distinct_count)
    return distinct_counts

k = int(input("Enter the window size:"))
result = distinct_window(arr, k)
print("Distinct counts in each window:", result)