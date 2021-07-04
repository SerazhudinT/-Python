def cubes(arr):
    return list(map(lambda x: x**3, arr))


def func(n, arr, i):
    while sum(cubes(arr)) < n:
        arr[i] += 1
        
        if i > 0:
            func(n, arr, i - 1)
    
    if sum(cubes(arr)) == n:
        return arr
        
    arr[i] = 0
    
    if sum(arr) == 0:
        if i == 6:
            return arr
        
        return func(n, arr, i + 1)



n = int(input())

arr = func(n, 7 * [0], 0)

if sum(arr) == 0:
    print(0)
else:
    print(*cubes(arr)[:7 - arr.count(0)])
