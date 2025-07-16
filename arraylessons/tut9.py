# finding the repetitive elemetns of an array.
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
arr.sort()
print("Sorted array:", arr)

def repetitive_elements():
    rep=[]
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            if arr[i] not in rep:
                rep.append(arr[i])
    print("The repetitive elements are:", rep)

repetitive_elements()