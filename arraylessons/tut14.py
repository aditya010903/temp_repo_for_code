from collections import Counter

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

def k_smallest_element():
    k = int(input("enter the value of k:"))
    arr.sort()
    print("the {}th smallest element is {}" .format(k,arr[k-1]))

k_smallest_element()