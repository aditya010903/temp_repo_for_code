# deducing the median of two sorted arrays after merging them
def input_array(size, array_num):
    array = []
    print(f"Enter {size} elements for array {array_num}:")
    for i in range(size):
        element = int(input(f"Element {i+1}: "))
        array.append(element)
    return array

size = int(input("Enter the size of the arrays: "))
array1 = input_array(size, 1)
array2 = input_array(size, 2)
array1.sort()
array2.sort()
print("Array 1:", array1)
print("Array 2:", array2)

def median_of_sorted_arrays():
    arr= array1 + array2
    arr.sort()
    print("Combined sorted arrays:", arr)
    n = len(arr)
    if n%2 == 0:
        median = (arr[n//2] + arr[n//2 - 1]) / 2
    elif n%2 != 0:
        median = arr[n//2]
    print("Median of the combine sorted arrays is : {}" .format(median))

median_of_sorted_arrays()
