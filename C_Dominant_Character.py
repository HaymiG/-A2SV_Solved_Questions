t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = -1

  
    for i in range(n - 1):
        sub = s[i:i+2]
        if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
            ans = 2
            break

   
    if ans == -1:
        for i in range(n - 2):
            sub = s[i:i+3]
            if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                ans = 3
                break

    print(ans)
