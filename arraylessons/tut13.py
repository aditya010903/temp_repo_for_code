# finding the majority element of an array. (element that appears more than n/2 times)
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
count = Counter(arr)
print(count)
if max(count.values())> len(arr)/2:
    print("Majority element is", max(count, key = count.get))