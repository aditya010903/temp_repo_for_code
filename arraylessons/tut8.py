# number of jumps to reach the end of the array.
def get_array():
    arr = []
    while len(arr) < 8:
        try:
            num = int(input(f"Enter integer {len(arr) + 1}: "))
            arr.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return arr

arr = get_array()
# arr.sort()
jump_count = 0
i = 0
print("Array:", arr)

while i < len(arr):
    jump = arr[i]
    if jump == 0:
        print("No jumps")
        break
    else:
        i += jump
        jump_count += 1

print("Number of jumps:", jump_count)