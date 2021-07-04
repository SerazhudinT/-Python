def CountSort(arr):
    sort = 101 * [0]

    for elem in arr:
        sort[elem] += 1

    k = 0

    for i in range(101):
        arr[k:k + sort[i]] = sort[i] * [i]

        k += sort[i]


arr = list(map(int, input().split()))

CountSort(arr)

print(*arr)
