# Write a program to print all the leaders in the array. An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
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

def array_leaders(arr):
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    
    leaders.reverse()
    print("The leaders in the array are:", leaders)

array_leaders(arr)