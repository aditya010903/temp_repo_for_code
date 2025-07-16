def array_leaders():
    leaders=[]
    compare=[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            compare.append(arr[j])
            compare.sort()
            if arr[i] > compare[-1]:
                if arr[i] not in leaders:
                    leaders.append(arr[i])
                    compare.clear()
    leaders.append(arr[-1])
    print("The leaders in the array are:", leaders)
 
array_leaders()