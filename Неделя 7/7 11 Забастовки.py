N, K = map(int, input().split())

days = list(range(N + 1))

strike = set()

for i in range(K):
    a, b = map(int, input().split())
    
    strike |= set(days[a::b])
    
strike -= set(days[6::7]) | set(days[7::7])

print(len(strike))
    
