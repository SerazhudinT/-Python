def func(n, arr, i):
    while arr[0]**2 + arr[1]**2 + arr[2]**2 + arr[3]**2 < n:
        arr[i] += 1
        
        if i > 0:
            func(n, arr, i - 1)
    
    if arr[0]**2 + arr[1]**2 + arr[2]**2 + arr[3]**2 == n:
        return arr
        
    arr[i] = 0
    
    if arr[0] + arr[1] + arr[2] + arr[3] == 0:
        return func(n, arr, i + 1)

n = int(input())

arr = func(n, 4 * [0], 0)

print(*arr[:4 - arr.count(0)])
