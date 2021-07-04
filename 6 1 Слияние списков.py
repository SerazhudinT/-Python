def merge(A, B):
    C = []
    
    i = j = 0
    while i < len(A) or j < len(B):
        if i < len(A) and (j == len(B) or A[i] < B[j]):
            C.append(A[i])

            i += 1
        elif j < len(B) and (i == len(A) or A[i] > B[j]):
            C.append(B[j])

            j += 1
        elif A[i] == B[j]:
            C.append(A[i])
            C.append(B[j])

            i += 1
            j += 1
        
    return C

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*merge(A, B))
