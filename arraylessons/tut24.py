def permutations(a):
    if len(a) == 0:
        return []
    if len(a) == 1:
        return [a]

    
    l = []
    for i in range(len(a)):
        m = a[i]
        rem = a[:i] + a[i+1:]
        for p in permutations(rem):
            l.append([m] + p)
    return l


user_input = input("Enter a string: ")
a = list(user_input)


result = permutations(a)

result = [''.join(p) for p in result]

print("The permutations of the given string are: {}".format(result))