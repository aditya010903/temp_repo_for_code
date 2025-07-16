# finding the peak elements of an array. (elements greater than their adjacent neighbors)
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

def peak_elements():
    peak = []
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            peak.append(arr[i])
    if arr[0]>arr[1]:
        peak.append(arr[0])
        if arr[-1]>arr[-2]:
            peak.append(arr[-1])
    elif arr[-1]>arr[-2]:
        peak.append(arr[-1])

    print("The peak elements are:", peak)


peak_elements()