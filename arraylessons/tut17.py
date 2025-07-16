# finding the longest subarray of equal numbers of zeros and ones.
def get_array():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    while len(arr) < n:
        try:
            num = int(input(f"Enter integer {len(arr) + 1}: "))
            arr.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return arr

arr = get_array()

def longest_subarray_of_equal_zeros_and_ones():
    count = 0
    max_len = 0
    count_map = {0: -1}  
    for i in range(len(arr)):
        if arr[i] == 0:
            count -= 1
        else:
            count += 1

        if count in count_map:
            max_len = max(max_len, i - count_map[count])
        else:
            count_map[count] = i

    print("The longest subarray of equal zeros and ones is of length:", max_len)

longest_subarray_of_equal_zeros_and_ones()