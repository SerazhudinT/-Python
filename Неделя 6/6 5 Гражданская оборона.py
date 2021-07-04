n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

a = []
b = []

for i in range(n):
    a.append((arr1[i], i + 1))
    
for i in range(m):
    b.append((arr2[i], i + 1))

a.sort()
b.sort()

result = n * [0]

begin = 0

for i in range(n):
    
    minDist = abs(a[i][0] - b[0][0])
     
    for j in range(begin, m):
        if minDist >= abs(a[i][0] - b[j][0]):
            minDist = abs(a[i][0] - b[j][0])
            
            result[a[i][1] - 1] = b[j][1]
            
            begin = j
        else:
            break
                 
print(*result)
