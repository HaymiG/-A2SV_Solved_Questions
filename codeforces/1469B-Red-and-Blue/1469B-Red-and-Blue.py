def max_prefix_sum(arr):
    cur_sum  = 0
    max_val = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        max_val = max(max_val, cur_sum)
    return max_val

t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    ans = max_prefix_sum(r) + max_prefix_sum(b)
    print(ans)