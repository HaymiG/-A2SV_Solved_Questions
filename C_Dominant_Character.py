t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    ans = -1

   
    for i in range(n - 1):
        if s[i] == 'a' and s[i + 1] == 'a':
            ans = 2
            break

   
    if ans == -1:
        for i in range(n - 2):
            sub = s[i:i + 3]
            if sub.count('a') == 2:
                ans = 3
                break

    print(ans)
