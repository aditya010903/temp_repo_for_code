size = int(input("Enter the size of the arrays: "))

array1 = []
array2 = []

print("Enter the elements for the first array:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    array1.append(element)

print("Enter the elements for the second array:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    array2.append(element)

print("First array:", array1)
print("Second array:", array2)

def union_without_duplicates(array1, array2):
    union = []
    for element in array1:
        if element not in union:
            union.append(element)
    for element in array2:
        if element not in union:
            union.append(element)
    union.sort()
    print("union of the two arrays after removing duplicates is : {}" .format(union))

union_without_duplicates(array1, array2)