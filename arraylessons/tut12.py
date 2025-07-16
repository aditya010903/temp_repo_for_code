# finding the area of rainwater trapped in an array.
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

def rainwater_area():
    left_bound = arr[0]
    right_bound = arr[-1]
    n = len(arr)
    
    if n < 3:
        print("The area of rainwater trapped is: 0")
        return
    
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = arr[0]
    right_max[n - 1] = arr[n - 1]
    
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])
    
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])
    
    new_area = 0
    for i in range(1, n - 1):
        new_area += min(left_max[i], right_max[i]) - arr[i]
    
    print("The area of rainwater trapped is:", new_area)

rainwater_area()